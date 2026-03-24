# Market Risk Monitoring Dashboard (MFE 5150)

This project is a high-performance, client-side financial risk analytics dashboard that compares GARCH and EGARCH volatility models using **95% Value at Risk (VaR) Backtesting** and the **Kupiec POF Test**.

## How to Run the App

1.  **Install Requirements**  
    Ensure you have Python installed, then install the necessary dependencies:
    ```bash
    pip install streamlit
    ```

2.  **Execute the Application**  
    Run the application using the following command from the project root directory:
    ```bash
    streamlit run streamlit_app.py
    ```

3.  **Use the Dashboard**  
    The application will open in your default browser. You can then:
    *   Upload the provided `SP500_Presentation_2016-2026.csv` or `Gold_GLD.US_2016-2026.csv` files.
    *   Toggle **Technical Details (Nerd Mode)** to see the underlying LaTeX math for EGARCH and the Kupiec Test.
    *   Compare model performance based on **VaR violations** rather than just AIC.

## Architecture Note
The server-side component (`streamlit_app.py`) acts solely as a lightweight shell. All econometric modelling (Nelder-Mead optimization, MLE fitting, and backtesting) is performed **purely in JavaScript** on the client-side to ensure zero-latency interactions.
