{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7913c893",
   "metadata": {},
   "outputs": [],
   "source": [
    "class earthquk2():\n",
    "    def __init__(self, Earthquacks):\n",
    "      self.mag=Earthquacks.mag\n",
    "        \n",
    "\n",
    "    def magnitude_injecction(self):\n",
    "      for i in range(len(self.mag)):\n",
    "        if Earthquacks.iloc[i]['mag']< 2.0:\n",
    "          Earthquacks.iloc[i, Earthquacks.columns.get_loc('Magnitude_Word')] ='Noticable'\n",
    "        elif  Earthquacks.iloc[i]['mag'] < 4.0: \n",
    "          Earthquacks.iloc[i, Earthquacks.columns.get_loc('Magnitude_Word')] ='minor'\n",
    "        elif  Earthquacks.iloc[i]['mag'] < 5.0: \n",
    "          Earthquacks.iloc[i, Earthquacks.columns.get_loc('Magnitude_Word')] ='light'\n",
    "        elif  Earthquacks.iloc[i]['mag'] < 6.0: \n",
    "          Earthquacks.iloc[i, Earthquacks.columns.get_loc('Magnitude_Word')] ='moderate'\n",
    "        elif  Earthquacks.iloc[i]['mag'] < 7.0: \n",
    "          Earthquacks.iloc[i, Earthquacks.columns.get_loc('Magnitude_Word')] ='strong'\n",
    "        elif  Earthquacks.iloc[i]['mag'] < 8.0: \n",
    "          Earthquacks.iloc[i, Earthquacks.columns.get_loc('Magnitude_Word')] ='major'\n",
    "        else:\n",
    "          Earthquacks.iloc[i, Earthquacks.columns.get_loc('Magnitude_Word')] ='epic'"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
