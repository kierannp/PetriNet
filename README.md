# WDeStuP

## Domain
This project is a design studio for building and simulating petri net models. The Petri Net domain consists of places and transitions with arcs connects these two types of elements together. Petri net models can be contained within a folder.  

## Uses
Petri nets have been extensively used to describe discrete-event distributed systems, a class of systems that are of particular interest in computer science applications.

## Installation

To install run: 
- Change the BASE_DIR in .env
- `docker-compose build`
- `docker-compose up -d` x 2

Connect to the server at http://localhost:8888

## How to Model in the Design Studio

In the composistion tab on the left side of the scren is where models and folders are created. To instantiate one simply drag and drop the onto the center screen. Once a model is created simply double click the created model to enter inside, then drag and drop the Places and transitions desired onto the center screen. To create arcs hover over the place or transition then click and drag highlighted blue square to the place or transtion where the arc destination. 

## Classifying and Simulation

Once a model is created it can be simulated and classified in the PetriViz tab on the left side. To simulate the model navigate inside the model in the composition tab, then click the PetriViz tab, this pulls up the simulation of the model. Black rectangle indicate fireable transitions that will progress your model. To fire the fireable transitions double click. To classify your model hit the Classify button toward the top of the screen.  