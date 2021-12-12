"""
This is where the implementation of the plugin code goes.
The PythonPlug-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('PythonPlug')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class PythonPlug(PluginBase):
  def main(self):
    active_node = self.active_node
    core = self.core
    logger = self.logger
    META = self.META
    nodes = core.load_sub_tree(active_node)
    p2t, t2p = {}, {}
    for node in nodes:
      if core.is_instance_of(node, META["place"]):
        p2t[core.get_path(node)] = []
      if core.is_instance_of(node, META["transition"]):
        t2p[core.get_path(node)] = []
    for node in nodes:
      if core.is_instance_of(node, META["t2p"]):
        t2p[core.get_pointer_path(node,'src')].append(core.get_pointer_path(node,'dst'))
      if core.is_instance_of(node, META["p2t"]):
        p2t[core.get_pointer_path(node,'src')].append(core.get_pointer_path(node,'dst'))
    
    def checkFreeChoice(p2t, t2p):
      if len(p2t) == 0:
        return False
      trans_ins = {}
      for t in t2p.keys():
        trans_ins[t] = set()
        for place, trans in p2t.items():
          for t1 in trans:
            if t1 == t:
              trans_ins[t].add(place)
      for ins in trans_ins.values():
        total = 0
        for ins2 in trans_ins.values():
          if ins == ins2:
            total += 1
        if total != 1:
          return False
      return True
    
    def checkStateMachine(p2t, t2p):
      total_ins = 0
      for t, p in t2p.items():
        total_ins = 0
        if len(set(p)) != 1:
          return False
        for place, trans in p2t.items():
          for t1 in set(trans):
            if t1 == t:
              total_ins += 1
      return False if total_ins != 1 else True
    
    def checkMarked(p2t, t2p):
      total_ins = 0
      for p, t in p2t.items():
        total_ins = 0
        if len(set(t)) != 1:
          return False
        for trans, places in t2p.items():
          for p1 in set(places):
            if p1 == p:
              total_ins += 1
      return False if total_ins != 1 else True
    
    def checkWorkflow(p2t, t2p):
      sources, sinks = 0, 0
      place_destinations = []
      for p in t2p.values():
        place_destinations.extend(p)
      for p, t in p2t.items():
        if not t:
          sinks += 1
        if p not in place_destinations:
          sources += 1
      if sources == 1 and sinks == 1:
        for p in t2p.values():
          if not p:
            return False
        return True
      else:
        return False
    
    self.send_notification('Your model is classified as:\
      \n Workflow: {}\n, FreeChoice: {}\n, Marked: {}\n, StateMachine: {}'.format(\
      checkWorkflow(p2t, t2p),\
        checkFreeChoice(p2t, t2p),\
           checkMarked(p2t, t2p),\
              checkStateMachine(p2t, t2p)))

