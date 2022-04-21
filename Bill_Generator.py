{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled2.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMC11nkXr7S7A+QGWkYoitc",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/parthpuneet03/100DofPy/blob/main/Bill_Generator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**TIP Calculator**"
      ],
      "metadata": {
        "id": "zAUS2IOMUVWv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a= float(input(\"Enter the bill amount: \"))\n",
        "b= int(input(\"ENter the percentage of tip 10, 12 or 15: \"))\n",
        "c= int(input(\"Enter the no of people to split the bill\"))\n",
        "totamt= a+((b/100)*a)\n",
        "\n",
        "payeach=(totamt)/c\n",
        "final_amt= \"{:.2f}\".format(payeach)\n",
        "print(f\"Each person should pay: ${final_amt}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V-80om1_UYbO",
        "outputId": "689e081c-3d4f-46f1-da7c-3f7641bc421a"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the bill amount: 10\n",
            "ENter the percentage of tip 10, 12 or 15: 10\n",
            "Enter the no of people to split the bill2\n",
            "Each person should pay: $5.50\n"
          ]
        }
      ]
    }
  ]
}