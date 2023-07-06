# Chemical Structure VisualizationTool with Compound Information Retrieval
This is a Python code for creating a graphical user interface that allows the user to input the name of a chemical compound, retrieves its SMILES representation from PubChem, and displays the 2D structure of the molecule. The interface has two buttons, one for starting the process of generating the structure and another for exiting the interface.

The code uses the following libraries:

rdkit for working with chemical structures and SMILES strings
pygame for creating the graphical user interface
urllib for making HTTP requests to PubChem's API
pubchempy for accessing chemical information from PubChem's database
The Button class is defined to create instances of buttons with a specified position, image, and scale. The draw method of this class checks if the mouse is hovering over the button and if it has been clicked, and returns a Boolean value indicating whether the button has been clicked.

The get_formula function takes a SMILES string as input and returns the molecular formula of the compound as a string.

The get_mass function takes a SMILES string as input and returns the molecular weight of the compound as a float.

The main function Structure takes the name of a chemical compound as input, retrieves its SMILES string using PubChem's API, creates a Mol object from the SMILES string using rdkit, and generates a 2D image of the molecule using rdkit's Draw module. The image is displayed on the screen using pygame.
