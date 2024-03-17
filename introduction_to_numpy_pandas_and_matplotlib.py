{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/shabinshad/python-introduction/blob/main/introduction_to_numpy_pandas_and_matplotlib.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "metadata": {
        "_uuid": "e829dfe21eb6f932696dcc1346f2a821aab41114",
        "id": "Fy-MClUYlXSn"
      },
      "cell_type": "markdown",
      "source": [
        "# <span style=\"color:red\"> Introduction to NumPy, Pandas and Matplotlib </span>"
      ]
    },
    {
      "metadata": {
        "_uuid": "c9b7c9d03d7d0b526583a4aad8896ce78ed8b8dc",
        "id": "qGzmgb5mlXSv"
      },
      "cell_type": "markdown",
      "source": [
        "## <span style=\"color:blue\"> Data Analysis </span>"
      ]
    },
    {
      "metadata": {
        "_uuid": "b88b4cc9b3eae8d2a5178a0df022738a62e3e575",
        "id": "beICpd6LlXSw"
      },
      "cell_type": "markdown",
      "source": [
        "Data Analysis is a process of inspecting, cleaning, transforming, and modeling data with the goal of discovering useful information, suggesting conclusions, and supporting decision-making."
      ]
    },
    {
      "metadata": {
        "_uuid": "d9b62f8552c6e1b2625e216ee5fe663cd3915815",
        "id": "w2YquPmElXSw"
      },
      "cell_type": "markdown",
      "source": [
        "Stpes for Data Analysis, Data Manipulation and Data Visualization:\n",
        "1. Tranform Raw Data in a Desired Format\n",
        "2. Clean the Transformed Data (Step 1 and 2 also called as a Pre-processing of Data)\n",
        "3. Prepare a Model\n",
        "4. Analyse Trends and Make Decisions"
      ]
    },
    {
      "metadata": {
        "_uuid": "b5164a9222662a7b85c0ca33715a5dcb42fb80f1",
        "id": "pU2hBQjklXSw"
      },
      "cell_type": "markdown",
      "source": [
        "## <span style=\"color:blue\"> NumPy </span>"
      ]
    },
    {
      "metadata": {
        "_uuid": "511de43c14f77c30297d793b83910f5cf3f708a5",
        "id": "xTyeIMqmlXSw"
      },
      "cell_type": "markdown",
      "source": [
        "NumPy is a package for scientific computing.\n",
        "1. Multi dimensional array\n",
        "2. Methods for processing arrays\n",
        "3. Element by element operations\n",
        "4. Mathematical operations like logical, Fourier transform, shape manipulation, linear algebra and random number generation"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "08c7be017b26d279f29cc310e8e4d963d4ae2da2",
        "id": "s4oWTcAzlXSx"
      },
      "cell_type": "code",
      "source": [
        "import numpy as np"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "9d775a851fc9ad7b84f4b16266f02561f1ffb12d",
        "id": "omAVogMNlXSx"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Ndarray - NumPy Array </span>"
      ]
    },
    {
      "metadata": {
        "_uuid": "3bc220d56c3b07beed11029091e9c7787e99f753",
        "id": "yF8KmZX7lXSx"
      },
      "cell_type": "markdown",
      "source": [
        "The ndarray is a multi-dimensional array object consisting of two parts -- the actual data, some metadata which describes the stored data. They are indexed just like sequence are in Python, starting from 0\n",
        "1. Each element in ndarray is an object of data-type object called dtype\n",
        "2. An item extracted from ndarray, is represented by a Python object of an array scalar type"
      ]
    },
    {
      "metadata": {
        "_uuid": "45cfdeebd3976fa47f5ce79bccf379196371e55b",
        "id": "f7tob3LhlXSy"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:green\"> Single Dimensional Array </span>"
      ]
    },
    {
      "metadata": {
        "_uuid": "989e570fe8b7b3bf1d3fce5d53d8d953bd38ff15",
        "id": "rs01fdd5lXSy"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Creating a Numpy Array </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "5a05543b043853c0e56055efdd424ca407d21d54",
        "id": "D1ZpLAQClXSy"
      },
      "cell_type": "code",
      "source": [
        "# Creating a single-dimensional array\n",
        "a = np.array([1,2,3]) # Calling the array function\n",
        "print(a)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "6b1bb7ccac0ef9e1bb10ae32067d657f4ad41d9b",
        "id": "E4Wv1G3TlXSy"
      },
      "cell_type": "code",
      "source": [
        "# Creating a multi-dimensional array\n",
        "# Each set of elements within a square bracket indicates a row\n",
        "# Array of two rows and two columns\n",
        "b = np.array([[1,2], [3,4]])\n",
        "print(b)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "f51dd35c6086518fdee722aadadd73737a31cfca",
        "id": "XW87Do_9lXSy"
      },
      "cell_type": "code",
      "source": [
        "# Creating an ndarray by wrapping a list\n",
        "list1 = [1,2,3,4,5] # Creating a list\n",
        "arr = np.array(list1) # Wrapping the list\n",
        "print(arr)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "da1fb0cf270ff4952d9212593c15dc35af0c2924",
        "id": "FICmcWN7lXSz"
      },
      "cell_type": "code",
      "source": [
        "# Creating an array of numbers of a specified range\n",
        "arr1 = np.arange(10, 100) # Array of numbers from 10 up to and excluding 100\n",
        "print(arr1)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "b4005dd1d350d82e2495c15e31a763108492f720",
        "id": "NhXbNAI5lXSz"
      },
      "cell_type": "code",
      "source": [
        "# Creating a 5x5 array of zeroes\n",
        "arr2 = np.zeros((5,5))\n",
        "print(arr2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "0cb37460c80a903c9b30148d4316278130481d0d",
        "id": "NKVo636qlXSz"
      },
      "cell_type": "code",
      "source": [
        "# Creating a linearly spaced vector, with spacing\n",
        "vector = np.linspace(0, 20, 5) # Start, stop, step\n",
        "print(vector)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "fe579e99445ed895fbf948723d1b4b3294a0f38f",
        "id": "1Yxk06uqlXSz"
      },
      "cell_type": "code",
      "source": [
        "# Creating Arrays from Existing Data\n",
        "x = [1,2,3]\n",
        "# Used for converting Python sequences into ndarrays\n",
        "c = np.asarray(x) #np.asarray(a, dtype = None, order = None)\n",
        "print(c)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "e7d3a247e74a3e225aef62fd82f28daad313e4d0",
        "id": "1S7dE0OUlXSz"
      },
      "cell_type": "code",
      "source": [
        "# Converting a linear array of 8 elements into a 2x2x2 3D array\n",
        "arr3 = np.zeros(8) # Flat array of eight zeroes\n",
        "arr3d = arr3.reshape((2,2,2)) # Restructured array\n",
        "print(arr3d)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "c30ef25050592ce5a900713de2456181e8d8da3a",
        "id": "h5O7fhSilXSz"
      },
      "cell_type": "code",
      "source": [
        "# Flatten rgw 3d array to get back the linear array\n",
        "arr4 = arr3d.ravel()\n",
        "print(arr4)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "8e8318d564d9d9beeb914c87fd44d8959ec90cb5",
        "id": "pKEHiMVelXSz"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Indexing of NumPy Arrays </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "598f958c1b21eba42ae4a5bebc3945085412c0ae",
        "id": "R2PRcAeilXS0"
      },
      "cell_type": "code",
      "source": [
        "# NumPy array indexing is identical to Python's indexing scheme\n",
        "arr5 = np.arange(2, 20)\n",
        "element = arr5[6]\n",
        "print(element)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "6fea915f4f4e21dba0134e29839d4c0315db87b4",
        "id": "Y1-j3RxslXS0"
      },
      "cell_type": "code",
      "source": [
        "# Python's concept of lists slicing is extended to NumPy.\n",
        "# The slice object is constructed by providing start, stop, and step parameters to slice()\n",
        "arr6 = np.arange(20)\n",
        "arr_slice = slice(1, 10, 2) # Start, stop & step\n",
        "element2 = arr6[6]\n",
        "print(arr6[arr_slice])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "60f5e32d48848bcb22cf159f7c90f4b962785897",
        "id": "zT3riGvUlXS0"
      },
      "cell_type": "code",
      "source": [
        "# Slicing items beginning with a specified index\n",
        "arr7 = np.arange(20)\n",
        "print(arr7[2:])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "5407ed48df87cfd936330f2fdf5b6b1b8df4add9",
        "id": "51o4dBMZlXS0"
      },
      "cell_type": "code",
      "source": [
        "# Slicing items until a specified index\n",
        "print(arr7[:15])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "5a4e22182b627ce467d8208050fd534c74f554b5",
        "id": "0B44Yx9hlXS0"
      },
      "cell_type": "code",
      "source": [
        "# Extracting specific rows and columns using Slicing\n",
        "d = np.array([[1,2,3], [3,4,5], [4,5,6]])\n",
        "print(d[0:2, 0:2]) # Slice the first two rows and the first two columns"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "1611c831b12cbd9f9a99f1e6abc72a38a5cd413f",
        "id": "cXsYUvkjlXS0"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> NumPy Array Attributes </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "65fa3b450304e43d42ca7e749a7da9d45c287902",
        "id": "Qu72WYGAlXS0"
      },
      "cell_type": "code",
      "source": [
        "print(d.shape) # Returns a tuple consisting of array dimensions\n",
        "print(d.ndim) # Attribute returns the number of array dimensions\n",
        "print(a.itemsize) # Returns the length of each element of array in bytes"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "ca39c694460aceb9e7a04fc746c21f618034d930",
        "id": "o2FOg9TvlXS0"
      },
      "cell_type": "code",
      "source": [
        "y = np.empty([3,2], dtype = int) # Creates an uninitialized array of specified shape and dtype\n",
        "print(y)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "3ba1fd700bd7a9adc0f88b6edf91b0dac60ef4f4",
        "id": "li9OrPGblXS0"
      },
      "cell_type": "code",
      "source": [
        "# Returns a new array of specified size, filled with zeros\n",
        "z = np.zeros(5) # np.zeros(shape, dtype = float)\n",
        "print(z)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "2619456897a5f6e5c18b78bdc15f75842a0bb5e6",
        "id": "vVCOGGHtlXS0"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Reading & Writing from Files </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "1d2969b2a7bb0a06a62cd3bddc55c0a0fc252f7b",
        "id": "Veucr6CYlXS1"
      },
      "cell_type": "code",
      "source": [
        "# NumPy provides the option of importing data from files directly into ndarray using the loadtxt function\n",
        "# The savetxt function can be used to write data from an array into a text file\n",
        "#import os\n",
        "#print(os.listdir('../input'))\n",
        "arr_txt = np.loadtxt('../input/data_file.txt')\n",
        "np.savetxt('newfilex.txt', arr_txt)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "f62d1c9aa9cac65306e433bbbbe06e50a436c92e",
        "id": "r6LcuH9flXS1"
      },
      "cell_type": "code",
      "source": [
        "# NumPy arrays can be dumped into CSV files using the savetxt function and the comma delimiter\n",
        "# The genfromtxt function can be used to read data from a CSV file into a NumPy array\n",
        "arr_csv = np.genfromtxt('../input/Hurricanes.csv', delimiter = ',')\n",
        "np.savetxt('newfilex.csv', arr_csv, delimiter = ',')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "a38b047cdd6a7080ff285508f5f1cb7129f9a7c1",
        "id": "7fzG_VXSlXS1"
      },
      "cell_type": "markdown",
      "source": [
        "## <span style=\"color:blue\"> Pandas </span>"
      ]
    },
    {
      "metadata": {
        "_uuid": "3b26c19b1903e0d95dacc1311519a88378f30303",
        "id": "q9zLsLuYlXS1"
      },
      "cell_type": "markdown",
      "source": [
        "Pandas is an open-source Python library providing efficient, easy-to-use data structure and data analysis tools. The name Pandas is derived from \"Panel Data\" - an Econometrics from Multidimensional Data. Pandas is well suited for many different kinds of data:\n",
        "1. Tabular data with heterogeneously-type columns.\n",
        "2. Ordered and unordered time series data.\n",
        "3. Arbitary matrix data with row and column labels.\n",
        "4. Any other form observational/statistical data sets. The data actually need not be labeled at all to be placed into a pandas data structure."
      ]
    },
    {
      "metadata": {
        "_uuid": "cf78f2b9bacaa59e12a7e2e61aff46dff1f666dd",
        "id": "l8ly3Ti-lXS1"
      },
      "cell_type": "markdown",
      "source": [
        "Pandas provides three data structure - all of which are build on top of the NumPy array - all the data structures are value-mutable\n",
        "1. Series (1D) - labeled, homogenous array of immutable size\n",
        "2. DataFrames (2D) - labeled, heterogeneously typed, size-mutable tabular data structures\n",
        "3. Panels (3D) - Labeled, size-mutable array"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "38adb2d5da62d084057781b45de06f95cb3ed1e5",
        "id": "26vLcNA2lXS1"
      },
      "cell_type": "code",
      "source": [
        "import pandas as pd"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "d21ec7b9f4e4fe941d18bf3fb10d4960ad10359a",
        "id": "_LLkWrOqlXS1"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Series </span>"
      ]
    },
    {
      "metadata": {
        "_uuid": "bae41f67082d4d920b8c9832cb3a60899cfe71d6",
        "id": "rYNLb8kmlXS1"
      },
      "cell_type": "markdown",
      "source": [
        "1. A Series is a single-dimensional array structures that stores homogenous data i.e., data of a single type.\n",
        "2. All the elements of a Series are value-mutable and size-immutable\n",
        "3. Data can be of multiple data types such as ndarray, lists, constants, series, dict etc.\n",
        "4. Indexes must be unique, hashable and have the same length as data. Defaults to np.arrange(n) if no index is passed.\n",
        "5. Data type of each column; if none is mentioned, it will be inferred; automatically\n",
        "6. Deep copies data, set to false as default"
      ]
    },
    {
      "metadata": {
        "_uuid": "4c32ac1eb23d07db65fbdf7250f389a5b04f82b5",
        "id": "xcMWFIiglXS2"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Creating a Series </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "5ed63fa17b2b538e539daab302d67114c258cc42",
        "id": "K0X7r1OilXS2"
      },
      "cell_type": "code",
      "source": [
        "# Creating an empty Series\n",
        "series = pd.Series() # The Series() function creates a new Series\n",
        "print(series)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "a9cfc77a3db1afb393811ab0307faac08fe39460",
        "id": "nNgnUMgFlXS2"
      },
      "cell_type": "code",
      "source": [
        "# Creating a series from an ndarray\n",
        "# Note that indexes are a assigned automatically if not specifies\n",
        "arr = np.array([10,20,30,40,50])\n",
        "series1 = pd.Series(arr)\n",
        "print(series1)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "1201e00798671b9bac1a3403b1d5583d35986850",
        "id": "r9y0yF2blXS2"
      },
      "cell_type": "code",
      "source": [
        "# Creating a series from a Python dict\n",
        "# Note that the keys of the dictionary are used to assign indexes during conversion\n",
        "data = {'a':10, 'b':20, 'c':30}\n",
        "series2 = pd.Series(data)\n",
        "print(series2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "2ea35ad1409457953e5f77c6ca9fd67a98e9ff2e",
        "id": "_QyZgtUdlXS2"
      },
      "cell_type": "code",
      "source": [
        "# Retrieving a part of the series using slicing\n",
        "print(series1[1:4])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "708e0e057e001451d59746cce980253ff00ca4c2",
        "id": "MFRdTDHglXS2"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> DataFrames </span>"
      ]
    },
    {
      "metadata": {
        "_uuid": "daa0ab53912a912ccc020f2faca4107e3c5fae93",
        "id": "RxS8BatFlXS2"
      },
      "cell_type": "markdown",
      "source": [
        "1. A DataFrame is a 2D data structure in which data is aligned in a tabular fashion consisting of rows & columns\n",
        "2. A DataFrame can be created using the following constructor - pandas.DataFrame(data, index, dtype, copy)\n",
        "3. Data can be of multiple data types such as ndarray, list, constants, series, dict etc.\n",
        "4. Index Row and column labels of the dataframe; defaults to np.arrange(n) if no index is passed\n",
        "5. Data type of each column\n",
        "6. Creates a deep copy of the data, set to false as default"
      ]
    },
    {
      "metadata": {
        "_uuid": "d3598cac5d32d3297b2ca111f5c0e2f235bc4a0e",
        "id": "er3-qKpylXS6"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Creating a DataFrame </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "227c5d6f90ad6d56a34f085ceb61b4c5fed276cc",
        "id": "8LyCIPiflXS6"
      },
      "cell_type": "code",
      "source": [
        "# Converting a list into a DataFrame\n",
        "list1 = [10, 20, 30, 40]\n",
        "table = pd.DataFrame(list1)\n",
        "print(table)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "7ded0db32d7b0fc09128aaf2e5491d8f73a87426",
        "id": "9iMwxyRVlXS7"
      },
      "cell_type": "code",
      "source": [
        "# Creating a DataFrame from a list of dictionaries\n",
        "data = [{'a':1, 'b':2}, {'a':2, 'b':4, 'c':8}]\n",
        "table1 = pd.DataFrame(data)\n",
        "print(table1)\n",
        "# NaN (not a number) is stored in areas where no data is provided"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "1c0542d329e786a77a142b89088d8895f69cd716",
        "id": "5w7CyvLclXS7"
      },
      "cell_type": "code",
      "source": [
        "# Creating a DataFrame from a list of dictionaries and accompaying row indices\n",
        "table2 = pd.DataFrame(data, index = ['first', 'second'])\n",
        "# Dict keys become column lables\n",
        "print(table2)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "4d2c55d48beb731c5524fa4513500844ea1c0746",
        "id": "avV2MCmBlXS7"
      },
      "cell_type": "code",
      "source": [
        "# Converting a dictionary of series into a DataFrame\n",
        "data1 = {'one':pd.Series([1,2,3], index = ['a', 'b', 'c']),\n",
        "        'two':pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd'])}\n",
        "table3 = pd.DataFrame(data1)\n",
        "print(table3)\n",
        "# the resultant index is the union of all the series indexes passed"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "2cf4ac79f04f67e5852d4e9631676c97252859b9",
        "id": "luTN38lplXS7"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> DataFrame - Addition & Deletion of Columns </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "235327bdb0eaf8476a8d66b49765215dfab464ba",
        "id": "9lOwm9VllXS7"
      },
      "cell_type": "code",
      "source": [
        "# A new column can be added to a DataFrame when the data is passed as a Series\n",
        "table3['three'] = pd.Series([10,20,30], index = ['a', 'b', 'c'])\n",
        "print(table3)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "6374a26f589f7d361fd8239674ecaeba0ec7bbf1",
        "id": "kWG39EuwlXS7"
      },
      "cell_type": "code",
      "source": [
        "# DataFrame columns can be deleted using the del() function\n",
        "del table3['one']\n",
        "print(table3)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "e4fa44918c61d8dbeb3a00ac1e18d4bf6a5ff712",
        "id": "--WhQdb3lXS7"
      },
      "cell_type": "code",
      "source": [
        "# DataFrame columns can be deleted using the pop() function\n",
        "table3.pop('two')\n",
        "print(table3)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "48a19c1f6b546447587aaf1ab5ff7fc0a89ac6c7",
        "id": "OXgyhaESlXS8"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> DataFrame - Addition & Deletion of Rows </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "2eac69204e5dbdd9ce95a9d56ca175c6d0ee5118",
        "id": "NMarDRW4lXS8"
      },
      "cell_type": "code",
      "source": [
        "# DataFrame rows can be selected by passing the row lable to the loc() function\n",
        "print(table3.loc['c'])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "da79c9d4e4f2bb650780ae18284cedd85d29f564",
        "id": "AljzpuA-lXS8"
      },
      "cell_type": "code",
      "source": [
        "# Row selection can also be done using the row index\n",
        "print(table3.iloc[2])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "f1b6454c112417a9c4e6be5f4b72a36572ff5cd4",
        "id": "bpX9cbGhlXS8"
      },
      "cell_type": "code",
      "source": [
        "# The append() function can be used to add more rows to the DataFrame\n",
        "data2 = {'one':pd.Series([1,2,3], index = ['a', 'b', 'c']),\n",
        "        'two':pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd'])}\n",
        "table5 = pd.DataFrame(data2)\n",
        "table5['three'] = pd.Series([10,20,30], index = ['a', 'b', 'c'])\n",
        "row = pd.DataFrame([[11,13],[17,19]], columns = ['two', 'three'])\n",
        "table6 = table5.append(row)\n",
        "print(table6)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "143c1cb32ef90922dee7bef4cef27df3dd9037b7",
        "id": "wQc1VQcwlXS8"
      },
      "cell_type": "code",
      "source": [
        "# The drop() function can be used to drop rows whose labels are provided\n",
        "table7 = table6.drop('a')\n",
        "print(table7)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "17b7ebd2c04dbffb401162bf8da05ee13ebce397",
        "id": "XYQbq_WIlXS8"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Importing & Exporting Data </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "5a3eb1090913736f1f19a808d2dcf32f873d7de0",
        "id": "6S_D20eclXS8"
      },
      "cell_type": "code",
      "source": [
        "# Data can be loaded into DataFrames from input data stored in the CSV format using the read_csv() function\n",
        "table_csv = pd.read_csv('../input/Cars2015.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "5f36b9c05638af526e6960d971c140dbace933d1",
        "id": "4V1CYj0WlXS8"
      },
      "cell_type": "code",
      "source": [
        "# Data present in DataFrames can be written to a CSV file using the to_csv() function\n",
        "# If the specified path doesn't exist, a file of the same name is automatically created\n",
        "table_csv.to_csv('newcars2015.csv')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "65163b0f6c8767438c6c402297567b0daf8bda6c",
        "id": "BvXi3a3LlXS9"
      },
      "cell_type": "code",
      "source": [
        "# Data can be loaded into DataFrames from input data stored in the Excelsheet format using read_excel()\n",
        "sheet = pd.read_excel('cars2015.xlsx')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "41650dc13e896c4028bbeec8c676b65f16b5138c",
        "id": "9LNTBt2nlXS9"
      },
      "cell_type": "code",
      "source": [
        "# Data present in DataFrames can be written to a spreadsheet file using to_excel()\n",
        "#If the specified path doesn't exist, a file of the same name is automatically created\n",
        "sheet.to_excel('newcars2015.xlsx')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "904d2b7af43896885e018826a55aeef7f8aa4658",
        "id": "84Tf2zCLlXS9"
      },
      "cell_type": "markdown",
      "source": [
        "## <span style=\"color:blue\"> Matplotlib </span>"
      ]
    },
    {
      "metadata": {
        "_uuid": "68e4b1ea9c5851e816438a697f899bc63e1deb0d",
        "id": "ap-hzSTPlXS9"
      },
      "cell_type": "markdown",
      "source": [
        "1. Matplotlib is a Python library that is specially designed for the development of graphs, charts etc., in order to provide interactive data visualisation\n",
        "2. Matplotlib is inspired from the MATLAB software and reproduces many of it's features"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "f4b547e7fafdaad4999dde4dda46dad1cf31c89f",
        "id": "dqnF5xQklXS9"
      },
      "cell_type": "code",
      "source": [
        "# Import Matplotlib submodule for plotting\n",
        "import matplotlib.pyplot as plt"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "86a99764d719fab6d6f1f6e5ff108869eef15936",
        "id": "S5QkcPytlXS9"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Plotting in Matplotlib </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "d66714fdd84d0942fa729f7dc554b3e16b88fa6e",
        "id": "Siv56g1plXS9"
      },
      "cell_type": "code",
      "source": [
        "plt.plot([1,2,3,4]) # List of vertical co-ordinates of the points plotted\n",
        "plt.show() # Displays plot\n",
        "# Implicit X-axis values from 0 to (N-1) where N is the length of the list"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "0c69eb3c06ed11469232121e1e5b434da4a6c417",
        "id": "ODmDRkLAlXS9"
      },
      "cell_type": "code",
      "source": [
        "# We can specify the values for both axes\n",
        "x = range(5) # Sequence of values for the x-axis\n",
        "# X-axis values specified - [0,1,2,3,4]\n",
        "plt.plot(x, [x1**2 for x1 in x]) # vertical co-ordinates of the points plotted: y = x^2\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "3c48d1ee2591b04ac33ea2072e5ad0d1f23d177f",
        "id": "U8pJ1OTDlXS-"
      },
      "cell_type": "code",
      "source": [
        "# We can use NumPy to specify the values for both axes with greater precision\n",
        "x = np.arange(0, 5, 0.01)\n",
        "plt.plot(x, [x1**2 for x1 in x]) # vertical co-ordinates of the points plotted: y = x^2\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "5a85d8b3d7361d4490bb994bdc4b9ffb982b34b3",
        "id": "6H1yYm38lXS-"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Multiline Plots </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "89882db0d96110ab8372d085aaf7cb6a887283be",
        "id": "hNhTBxl3lXS-"
      },
      "cell_type": "code",
      "source": [
        "# Multiple functions can be drawn on the same plot\n",
        "x = range(5)\n",
        "plt.plot(x, [x1 for x1 in x])\n",
        "plt.plot(x, [x1*x1 for x1 in x])\n",
        "plt.plot(x, [x1*x1*x1 for x1 in x])\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "de97da239b07d2349f73a3390fff7e4b5c367e44",
        "id": "_UxPEj2OlXS-"
      },
      "cell_type": "code",
      "source": [
        "# Different colours are used for different lines\n",
        "x = range(5)\n",
        "plt.plot(x, [x1 for x1 in x],\n",
        "         x, [x1*x1 for x1 in x],\n",
        "         x, [x1*x1*x1 for x1 in x])\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "9cd45bf593f881c791bcff4d4c0fe1e5c61e1fc7",
        "id": "rZDn7sYqlXS-"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Grids </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "73b88ebef410242f116af8e509869af2a6ea19b9",
        "id": "ry3X2KkrlXS-"
      },
      "cell_type": "code",
      "source": [
        "# The grid() function adds a grid to the plot\n",
        "# grid() takes a single Boolean parameter\n",
        "# grid appears in the background of the plot\n",
        "x = range(5)\n",
        "plt.plot(x, [x1 for x1 in x],\n",
        "         x, [x1*2 for x1 in x],\n",
        "         x, [x1*4 for x1 in x])\n",
        "plt.grid(True)\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "231a396290779a9d8e52ed10fef8aa4bbe9d47fa",
        "id": "mNapHwGvlXS-"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Limiting the Axes </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "74034e58aeb7ae32b01ed7ae319f23348c349b22",
        "id": "qN7fNCYwlXS-"
      },
      "cell_type": "code",
      "source": [
        "# The scale of the plot can be set using axis()\n",
        "x = range(5)\n",
        "plt.plot(x, [x1 for x1 in x],\n",
        "         x, [x1*2 for x1 in x],\n",
        "         x, [x1*4 for x1 in x])\n",
        "plt.grid(True)\n",
        "plt.axis([-1, 5, -1, 10]) # Sets new axes limits\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "072cbd4d32eb29645ca3ee15f5281e5fa9c11e06",
        "id": "OA-cQm39lXS-"
      },
      "cell_type": "code",
      "source": [
        "# The scale of the plot can also be set using xlim() and ylim()\n",
        "x = range(5)\n",
        "plt.plot(x, [x1 for x1 in x],\n",
        "         x, [x1*2 for x1 in x],\n",
        "         x, [x1*4 for x1 in x])\n",
        "plt.grid(True)\n",
        "plt.xlim(-1, 5)\n",
        "plt.ylim(-1, 10)\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "8cc38d6770e2f10609866bf296fa15459b6fb7f3",
        "id": "z8dalQMTlXS_"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Adding Labels </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "be88c8566bda7feaaf9b9c8b70bcbd36892139d3",
        "id": "7uuE_m4elXS_"
      },
      "cell_type": "code",
      "source": [
        "# Labels can be added to the axes of the plot\n",
        "x = range(5)\n",
        "plt.plot(x, [x1 for x1 in x],\n",
        "         x, [x1*2 for x1 in x],\n",
        "         x, [x1*4 for x1 in x])\n",
        "plt.grid(True)\n",
        "plt.xlabel('X-axis')\n",
        "plt.ylabel('Y-axis')\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "5169d447c2d92d6fe31ee1c18179e6b11491858a",
        "id": "94GiPIvclXS_"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Adding the Title </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "b94aae589c431fb5fcecbe03f6570f437a7d0228",
        "id": "TXIpW00SlXS_"
      },
      "cell_type": "code",
      "source": [
        "# The title defines the data plotted on the graph\n",
        "x = range(5)\n",
        "plt.plot(x, [x1 for x1 in x],\n",
        "         x, [x1*2 for x1 in x],\n",
        "         x, [x1*4 for x1 in x])\n",
        "plt.grid(True)\n",
        "plt.xlabel('X-axis')\n",
        "plt.ylabel('Y-axis')\n",
        "plt.title(\"Polynomial Graph\") # Pass the title as a parameter to title()\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "172f61af59f5a8ad35c59ae3df347de5af35bce4",
        "id": "TRiFRym6lXS_"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Adding a Legend </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "814d4b6c6130370dee9ab6f9e99bc2e01b65fbbf",
        "id": "p5GybkqClXS_"
      },
      "cell_type": "code",
      "source": [
        "# Legends explain the meaning of each line in the graph\n",
        "x = np.arange(5)\n",
        "plt.plot(x, x, label = 'linear')\n",
        "plt.plot(x, x*x, label = 'square')\n",
        "plt.plot(x, x*x*x, label = 'cube')\n",
        "plt.grid(True)\n",
        "plt.xlabel('X-axis')\n",
        "plt.ylabel('Y-axis')\n",
        "plt.title(\"Polynomial Graph\")\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "57dff004230d951523b4a62ba9d6e809bd588f15",
        "id": "kwogGnQdlXS_"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Adding a Markers </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "21f95e777e4c6917c33bedf753f382a91e79633b",
        "id": "Ge7jkymQlXS_"
      },
      "cell_type": "code",
      "source": [
        "x = [1, 2, 3, 4, 5, 6]\n",
        "y = [11, 22, 33, 44, 55, 66]\n",
        "plt.plot(x, y, 'bo')\n",
        "for i in range(len(x)):\n",
        "    x_cord = x[i]\n",
        "    y_cord = y[i]\n",
        "    plt.text(x_cord, y_cord, (x_cord, y_cord), fontsize = 10)\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "98731e989a1f6d56ddd51ac5a11dd4e8b70f16e1",
        "id": "DDT1bzSzlXTA"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Saving Plots </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "f7805cfc4fe4a2fa21d52cb65c9e6dce59b19307",
        "id": "Uc1mCLjelXTA"
      },
      "cell_type": "code",
      "source": [
        "# Plots can be saved using savefig()\n",
        "x = np.arange(5)\n",
        "plt.plot(x, x, label = 'linear')\n",
        "plt.plot(x, x*x, label = 'square')\n",
        "plt.plot(x, x*x*x, label = 'cube')\n",
        "plt.grid(True)\n",
        "plt.xlabel('X-axis')\n",
        "plt.ylabel('Y-axis')\n",
        "plt.title(\"Polynomial Graph\")\n",
        "plt.legend()\n",
        "plt.savefig('plot.png') # Saves an image names 'plot.png' in the current directory\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "d29a166f7287ac8fb1546500d1f35e22551846bf",
        "id": "YOt9pzBYlXTA"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Plot Types </span>"
      ]
    },
    {
      "metadata": {
        "_uuid": "74861621a9e2c05cb3ad3f049c1cb7d4d7f8c898",
        "id": "bhtbt1CSlXTA"
      },
      "cell_type": "markdown",
      "source": [
        "Matplotlib provides many types of plot formats for visualising information\n",
        "1. Scatter Plot\n",
        "2. Histogram\n",
        "3. Bar Graph\n",
        "4. Pie Chart"
      ]
    },
    {
      "metadata": {
        "_uuid": "da78a859581c6ea5f494209ed5d1137e21bae067",
        "id": "hScA0eSilXTA"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Histogram </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "07f9d1e6cc0b19b171682b2569cff740944bcc99",
        "id": "m-fBoZEzlXTA"
      },
      "cell_type": "code",
      "source": [
        "# Histograms display the distribution of a variable over a range of frequencies or values\n",
        "y = np.random.randn(100, 100) # 100x100 array of a Gaussian distribution\n",
        "plt.hist(y) # Function to plot the histogram takes the dataset as the parameter\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "c48f91fe7b9049934d81529961d437deba41263e",
        "id": "rqDWVZkMlXTA"
      },
      "cell_type": "code",
      "source": [
        "# Histogram groups values into non-overlapping categories called bins\n",
        "# Default bin value of the histogram plot is 10\n",
        "y = np.random.randn(1000)\n",
        "plt.hist(y, 100)\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "1275a1de4261dcd82518f331378f69d7d358608b",
        "id": "RVWjqTkklXTA"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Bar Chart </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "a1f25ce1fe76a701fc83510efaccb5ab576b8636",
        "id": "jEh7LMmjlXTA"
      },
      "cell_type": "code",
      "source": [
        "# Bar charts are used to visually compare two or more values using rectangular bars\n",
        "# Default width of each bar is 0.8 units\n",
        "# [1,2,3] Mid-point of the lower face of every bar\n",
        "# [1,4,9] Heights of the successive bars in the plot\n",
        "plt.bar([1,2,3], [1,4,9])\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "c82164448b4ec1ff485cffd03ede3de7b31d3667",
        "id": "08Qo13hqlXTB"
      },
      "cell_type": "code",
      "source": [
        "dictionary = {'A':25, 'B':70, 'C':55, 'D':90}\n",
        "for i, key in enumerate(dictionary):\n",
        "    plt.bar(i, dictionary[key]) # Each key-value pair is plotted individually as dictionaries are not iterable\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "8e368f70500b7b7c603a60854f2525ac8f737edb",
        "id": "H0eNvRSZlXTB"
      },
      "cell_type": "code",
      "source": [
        "dictionary = {'A':25, 'B':70, 'C':55, 'D':90}\n",
        "for i, key in enumerate(dictionary):\n",
        "    plt.bar(i, dictionary[key])\n",
        "plt.xticks(np.arange(len(dictionary)), dictionary.keys()) # Adds the keys as labels on the x-axis\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "9195735d8fc3b6a42ad8c03c24f628ee1e715a32",
        "id": "1K2CBT2WlXTB"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Pie Chart </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "71823d0849f9ca477619d95940cd8c15da89898f",
        "id": "h92n8u_QlXTB"
      },
      "cell_type": "code",
      "source": [
        "plt.figure(figsize = (3,3)) # Size of the plot in inches\n",
        "x = [40, 20, 5] # Proportions of the sectors\n",
        "labels = ['Bikes', 'Cars', 'Buses']\n",
        "plt.pie(x, labels = labels)\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "d822c7ae1a456073223dc037cc9171040bbc7f84",
        "id": "QL4n14ZPlXTB"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Scatter Plot </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "6c0584e7fa4d5ee9a12b8912552a840ea7055955",
        "id": "6RZbif_vlXTB"
      },
      "cell_type": "code",
      "source": [
        "# Scatter plots display values for two sets of data, visualised as a collection of points\n",
        "# Two Gaussion distribution plotted\n",
        "x = np.random.rand(1000)\n",
        "y = np.random.rand(1000)\n",
        "plt.scatter(x, y)\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "f7581aa4d0b981323ee0749dead69228820b71e2",
        "id": "KISgX1rLlXTB"
      },
      "cell_type": "markdown",
      "source": [
        "### <span style=\"color:orange\"> Styling </span>"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "8bdecd2648a9546f7ce5855125a21ffc8fea30ce",
        "id": "6IQA5i0mlXTB"
      },
      "cell_type": "code",
      "source": [
        "# Matplotlib allows to choose custom colours for plots\n",
        "y = np.arange(1, 3)\n",
        "plt.plot(y, 'y') # Specifying line colours\n",
        "plt.plot(y+5, 'm')\n",
        "plt.plot(y+10, 'c')\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "_uuid": "04fc2ae81d1958f28bbbbac031ec2a068f071cb3",
        "id": "VVu-CXE3lXTB"
      },
      "cell_type": "markdown",
      "source": [
        "Color code:\n",
        "1. b = Blue\n",
        "2. c = Cyan\n",
        "3. g = Green\n",
        "4. k = Black\n",
        "5. m = Magenta\n",
        "6. r = Red\n",
        "7. w = White\n",
        "8. y = Yellow"
      ]
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "20cf6a6db7f23468ec7e0faa4d2e01207cd63f70",
        "id": "mEZCpNE4lXTC"
      },
      "cell_type": "code",
      "source": [
        "# Matplotlib allows different line styles for plots\n",
        "y = np.arange(1, 100)\n",
        "plt.plot(y, '--', y*5, '-.', y*10, ':')\n",
        "plt.show()\n",
        "# - Solid line\n",
        "# -- Dashed line\n",
        "# -. Dash-Dot line\n",
        "# : Dotted Line"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "metadata": {
        "trusted": true,
        "_uuid": "bd8de81dda276dc4517e302a628de7b35cd3886d",
        "id": "blNaN9yWlXTC"
      },
      "cell_type": "code",
      "source": [
        "# Matplotlib provides customization options for markers\n",
        "y = np.arange(1, 3, 0.2)\n",
        "plt.plot(y, '*',\n",
        "        y+0.5, 'o',\n",
        "        y+1, 'D',\n",
        "        y+2, '^',\n",
        "        y+3, 's') # Specifying line styling\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": "3.6.6",
      "mimetype": "text/x-python",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "file_extension": ".py"
    },
    "colab": {
      "provenance": [],
      "include_colab_link": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
