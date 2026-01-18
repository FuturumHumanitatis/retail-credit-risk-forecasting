-- Monthly portfolio mart (Greenplum-style)

SELECT
    report_date,
    product_type,
    COUNT(DISTINCT loan_id)        AS loans_cnt,
    SUM(balance)                  AS total_balance,
    AVG(dpd)                      AS avg_dpd,
    SUM(CASE WHEN dpd > 90 THEN balance ELSE 0 END) AS npl_balance
FROM loan_snapshot
GROUP BY report_date, product_type
ORDER BY report_date;
