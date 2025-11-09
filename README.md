# 🚗 Travel Fare Calculator

## 🧾 Overview
This Python program calculates the **travel fare** based on:
- The **distance** traveled (in kilometers)
- The **vehicle type** chosen (Bike, Car, or Bus)

It also provides:
- **Discounts** for high fares  
- **Travel suggestions** for long distances

---

## ⚙️ How It Works
1. The user enters:
   - **Name** of the passenger  
   - **Distance** (in km)  
   - **Vehicle type**  
     - `1` → Bike  
     - `2` → Car  
     - `3` → Bus  
2. The program calculates the fare using one of three functions:
   - `pricecalcbike(d)`
   - `pricecalccar(d)`
   - `pricecalcbus(d)`
3. A **5% discount** is applied if the fare exceeds ₹1500.  
4. If the distance is more than **500 km**, a travel suggestion is displayed.

---

## 💰 Fare Rates

| Vehicle | Up to 50 km | 51–200 km | Above 200 km |
|----------|--------------|------------|---------------|
| **Bike** | ₹5/km        | ₹4/km      | ₹3.5/km       |
| **Car**  | ₹10/km       | ₹9/km      | ₹8/km         |
| **Bus**  | ₹8/km        | ₹7/km      | ₹6/km         |

---

## 🧮 Sample Run
```bash
Enter your name: Dilshad
Enter the distance(in km): 180
choose the vehicle type (bike (1) car (2) bus (3)): 2
````

**Output:**

```text
passenger name: Dilshad
vehicle type: 2
Distance: 180.0 km
Base Fare: 1620.0 ₹
Discount(5%): 81.0 ₹
Total amount payable: 1539.0 ₹
```

---

## ▶️ How to Run

1. Save the code in a file named **fare_calculator.py**
2. Open a terminal or VS Code
3. Run the following command:

   ```bash
   python fare_calculator.py
   ```
4. Follow the prompts on the screen.

---

## 💡 Notes

* Enter valid inputs for distance and vehicle type.
* The program assumes base rates and does not include taxes or tolls.
* Works with **Python 3.x** and above.

---

## 🧑‍💻 Author

**Dilshad**
Travel Fare Calculator – A simple project to practice conditional statements and functions in Python.

```

---

Would you like me to add a **project badge and emoji-style design** (like "Made with Python 🐍" and GitHub badges)? It’ll make your README look more professional for uploading to GitHub.
```
