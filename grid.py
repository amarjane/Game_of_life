#!/usr/bin/env python
# coding: utf-8

"""Class grid with methods to change state of cells"""

import numpy as np
import logging

__author__ = "Abdelaziz Marjane"
__copyright__ = "Copyright 20, The Conway's Game of Life"
__credits__ = ["Abdelaziz Marjane"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Abdelaziz Marjane"
__email__ = "marjane.abdelaziz@gmail.fr"
__status__ = "Developement"

import pandas as pd


class LifeMatrix:
    """Class with methods to generate initial state et to transfor"""

    def __init__(self, p, n = 10, m = 10):
        logging.info("========================\nInitialisation Life Of Matrix\n========================")
        self._generation = 0
        self._nbr_lines = n
        self._nbr_cols = m
        self._probability = p
        self._state = np.random.choice([0, 1], size=(self._nbr_lines, self._nbr_cols), p=[1 - self._probability, self._probability])
        self.represent(self._state)
        logging.info("Matrix : \n" + np.array2string(self._state))
        logging.info("Shape : " + str(self._nbr_lines) + " x " + str(self._nbr_cols))
        logging.info("Probability : " + str(self._probability))
        logging.info("Representation : " +  self._representation)
        logging.info("Generation : " + str(self._generation))

    def transform(self):
        M = np.copy(self._state)
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                condition = self.transition(self._state, i, j)
                logging.debug('condition : ' + str(condition))
                if condition == 3:
                    M[i, j] = 1
                elif condition == 2:
                    M[i, j] = self._state[i, j]
                else:
                    M[i, j] = 0
        self._state = M
        self.represent(self._state)


    def transition(self, M, i, j):
        r = 0
        m = M.shape[0]
        n = M.shape[1]

        top = i-1 if i > 0 else 0
        bottom = i+1 if i < m-1 else i
        left = j-1 if j > 0 else 0
        right = j+1 if j < n-1 else j

        for line in range(top, bottom + 1):
            for col in range(left, right + 1):
                r += M[line, col]

        r -= M[i, j]

        return r

    def represent(self, M):
        logging.debug("Represent currently")
        new_representation = ""
        for i in range(M.shape[0]):
            line = ""
            for j in range(M.shape[1]):
                if M[i, j] == 0:
                    line += "x"
                if M[i, j] == 1:
                    line += "@"
            logging.debug("New line : " + line)
            new_representation += "\n" + line
        self._representation = new_representation
        logging.info("Representation : " + self._representation)

    def display(self):
        logging.info("Matrix : \n" + np.array2string(self._state))
        logging.info("Representation : " + self._representation)

    def _get_nbr_lines(self):
        return self._nbr_lines

    def _set_nbr_lines(self, m):
        self._nbr_lines = m

    def _get_nbr_cols(self):
        return self._nbr_cols

    def _set_nbr_cols(self, n):
        self._nbr_cols = n

    def _get_probability(self):
        return self._probability

    def _set_probability(self, p):
        self._probability = p

    def _get_state(self):
        return self._state

    def _set_state(self, S):
        self._state = S

    def _get_representation(self):
        return self._representation

    def _set_representation(self, str):
        self._representation = str

    nbr_lines = property(_get_nbr_lines, _set_nbr_lines, "Property nbr_lines")
    nbr_cols = property(_get_nbr_cols, _set_nbr_cols, "Property nbr columns")
    probability = property(_get_probability, _set_probability, "Property probability of 1")
    state = property(_get_state, _set_state, "Property state of the matrix of life")
    representation = property(_get_representation, _set_representation, "The representation of the binary matrix")


class GameOfLife:

    def __init__(self, g, p, n = 10, m = 10):
        logging.info("Initialisation of an instance of GameOfLife")
        self._LM = LifeMatrix(p, n, m)
        self._generation = g

    def _get_generation(self):
        return self._generation

    def _set_generation(self, g):
        self._generation = g

    def _get_LM(self):
        return self._LM

    def _set_LM(self, LM):
        self._LM = LM

    def run(self):
        logging.info("========================\nRunning Game of Life\n========================")
        i = 0
        while i < self._generation:
            logging.info("Generation : " + str(i))
            self._LM.display()
            self._LM.transform()
            i += 1

    generation = property(_get_generation, _set_generation, "Property generation")
    LM =  property(_get_LM, _set_LM, "Property generation")


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    GameOfLife(5, 0.2, *(7,7)).run()