from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    # define cost variables
    machinery_cost = 10000
    startup_capital = 50000
    fac_dep_annual = 25000
    raw_mtrl_annual = 10000
    labor_costs_annual = 5000
    various_exp_annual = 25000

    # define revenue variables
    annual_biz_revenue = 500000
    facility_resid_val = 100000
    recovered_wrk_capital = 75000

    # calculate ROI
    total_costs = machinery_cost + startup_capital + (fac_dep_annual * 10) + (raw_mtrl_annual * 10) + (labor_costs_annual * 10) + (various_exp_annual * 10)
    total_revenues = annual_biz_revenue * 10 + facility_resid_val + recovered_wrk_capital
    roi = (total_revenues - total_costs) / total_costs * 100

    # return ROI as a string
    return "The ROI for the beverage industry is: {:.2f}%".format(roi)

if __name__ == "__main__":
    app.run()
