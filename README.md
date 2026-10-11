# hotel-booking-demand-analysis
## 📌 What I Did in This Project

1. **Data Preparation & Cleaning:**
   - Loaded the dataset (`hotel_bookings.csv`) in Google Colab.
   - Handled missing values (filled empty `agent`/`company` with `0`, missing `country` with `'Unknown'`).
   - Cleaned up duplicate rows to make sure the insights are accurate.

2. **Exploratory Data Analysis (EDA):**
   - Analyzed key features including hotel types, lead time, pricing (ADR), and cancellation rates.
   - Created **5 visual plots** using `seaborn` and `matplotlib` (count plots, histogram with KDE, box plot, and a correlation heatmap).

3. **Key Findings:**
   - **Cancellations:** Bookings made way in advance (high lead time) and those with zero special requests have higher cancellation rates.
   - **Hotel Types:** City Hotels get higher overall demand, while Resort Hotels see price spikes during summer holidays.
   - **Peak Season:** July and August are the busiest months.

---

## 🛠️ Tools & Tech Stack
- **Language:** Python
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
- **Environment:** Google Colab / Jupyter Notebook

---

## 🚀 How to Run
1. Clone this repository or download `Hotel_Booking_Analysis.ipynb`.
2. Upload `hotel_bookings.csv` to your environment.
3. Run all cells in the notebook!
