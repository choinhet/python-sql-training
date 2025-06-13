import duckdb

if __name__ == "__main__":
    print("Store Share")
    duckdb.query(
        """
        select 
            StoreName,
            SUM(Value) as StoreSales,
            (SUM(SUM(Value)) OVER ()) as TotalSales,
            SUM(Value)/(SUM(SUM(Value)) OVER ()) as StoreShare
        from read_parquet('../resources/fact_sales.parquet') fact
        left join read_parquet('../resources/dim_store.parquet') store
            on fact.StoreId = store.StoreId
        group by StoreName
        order by StoreShare desc
        """
    ).show()
