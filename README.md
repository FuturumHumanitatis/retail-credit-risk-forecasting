
# Retail Credit Risk Forecasting

End-to-end аналитический проект по прогнозированию риск-метрик
розничного кредитного портфеля.

## Business Problem
Оценка PD и расчёт ожидаемых кредитных потерь (ECL) для целей
риск-менеджмента и планирования резервов.

## Stack
- Python (pandas, Polars, scikit-learn)
- SQL (Greenplum-style)
- Git

## Project Structure
- ETL и очистка данных
- Feature engineering
- PD-модель
- Forecast резервов (ECL)

## How to Run
```bash
pip install -r requirements.txt
python src/forecast.py
