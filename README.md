# Payslips Multi Currency

## 📌 Overview

**Payslips Multi Currency** is a custom Odoo module that enables payroll processing using the currency defined in each employee’s contract instead of relying only on the company’s default currency.

This allows each employee to have their salary, payslip computation, and report displayed in their own contract currency.

---

## 🚀 Features

* Add a **currency field** to employee contracts
* Each contract can define its own currency (e.g., EGP, USD, EUR)
* Payslips automatically use the contract currency
* Payslip computations are displayed in the selected currency
* Payroll reports are generated using the same contract currency
* Seamless integration with Odoo Payroll module

---

## 💡 Business Value

This module is useful for companies that:

* Have employees paid in different currencies
* Operate in multiple countries
* Want payroll reports aligned with contract currency instead of company currency

---

## ⚙️ How It Works

1. Open Employee Contract
2. Select the desired **Currency**
3. Create a Payslip for the employee
4. Click **Compute Sheet**
5. The payslip is generated using the contract currency
6. The printed report also reflects the same currency

---

## 📷 Screenshot

(https://github.com/maryam958/odoo-payslips-multi-currency/blob/main/contract.png)

---

## 📦 Installation

1. Clone the repository into your Odoo addons folder:

```bash
git clone https://github.com/your-username/payslips-multi-currency.git
```

2. Restart Odoo server

3. Update Apps List

4. Install the module **Payslips Multi Currency**

---

## 🔧 Requirements

* Odoo 17
* `hr_payroll` module

---

## 🧑‍💻 Technical Details

* Adds a currency field to `hr.contract`
* Overrides payslip computation logic
* Modifies report rendering to use contract currency

---

## 👩‍💻 Author

Maryam Mohamed

---

## 📄 License

LGPL-3
