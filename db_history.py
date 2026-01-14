{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18471d2c",
   "metadata": {},
   "outputs": [],
   "source": [
    "from app import db\n",
    "from models import QA\n",
    "\n",
    "# Fetch all entries\n",
    "entries = QA.query.all()\n",
    "for e in entries:\n",
    "    print(e.id, e.timestamp, e.question, e.answer)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.12.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
