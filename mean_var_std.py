
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 223,
   "id": "b7197b3a-010d-4939-bb1a-1e2642e5783a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "def calculate(list_input):\n",
    "    if len(list_input) != 9:\n",
    "        raise ValueError(\"List must contain nine number\")\n",
    "        \n",
    "    martix = np.array(list_input).reshape(3,3)\n",
    "\n",
    "    mean_axis1 = martix.mean(axis=0).tolist()\n",
    "    mean_axis2 = martix.mean(axis=1).tolist()\n",
    "    mean_flattened = martix.mean().tolist()\n",
    "\n",
    "    var_axis1 = martix.var(axis=0).tolist()\n",
    "    var_axis2 = martix.var(axis=1).tolist()\n",
    "    var_flattened = martix.var().tolist()\n",
    "\n",
    "    std_axis1 = martix.std(axis=0).tolist()\n",
    "    std_axis2 = martix.std(axis=1).tolist()\n",
    "    std_flattened = martix.std().tolist()\n",
    "\n",
    "    max_axis1 = martix.max(axis=0).tolist()\n",
    "    max_axis2 = martix.max(axis=1).tolist()\n",
    "    max_flattened = martix.max().tolist()\n",
    "\n",
    "    min_axis1 = martix.min(axis=0).tolist()\n",
    "    min_axis2 = martix.min(axis=1).tolist()\n",
    "    min_flattened = martix.min().tolist()\n",
    "\n",
    "    sum_axis1 = martix.sum(axis=0).tolist()\n",
    "    sum_axis2 = martix.sum(axis=1).tolist()\n",
    "    sum_flattened = martix.sum().tolist()\n",
    "\n",
    "    calculations = {\n",
    "        'mean': [mean_axis1, mean_axis2, mean_flattened],\n",
    "        'variance': [var_axis1, var_axis2, var_flattened],\n",
    "        'standard deviation': [std_axis1, std_axis2, std_flattened],\n",
    "        'max': [max_axis1, max_axis2, max_flattened],\n",
    "        'min': [min_axis1, min_axis2, min_flattened],\n",
    "        'sum': [sum_axis1, sum_axis2, sum_flattened]\n",
    "}\n",
    "    return caclcutions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 233,
   "id": "00694e4a-26d4-41ef-bb9e-cbfc0e4ec252",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "calculation successful :  {'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611], 'max': [[6, 7, 8], [2, 5, 8], 8], 'min': [[0, 1, 2], [0, 3, 6], 0], 'sum': [[9, 12, 15], [3, 12, 21], 36]}\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    result = calculate([0,1,2,3,4,5,6,7,8])\n",
    "    print(\"calculation successful : \",result)\n",
    "except ValueError as e:\n",
    "    print(\"Error\",e)"
   ]
  
