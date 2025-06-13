import duckdb

if __name__ == "__main__":
    print("Total Sales By Store")
    duckdb.query(
        """
        select 
            StoreName,
            SUM(Value) as TotalSales
        from read_parquet('../resources/fact_sales.parquet') fact
        left join read_parquet('../resources/dim_store.parquet') store
            on fact.StoreId = store.StoreId
        group by StoreName
        order by TotalSales desc
        """
    ).show()

    print("Total Sales By Product")
    duckdb.query(
        """
        select 
            ProductName,
            SUM(Value) as TotalSales
        from read_parquet('../resources/fact_sales.parquet') fact
        left join read_parquet('../resources/dim_product.parquet') product
            on fact.ProductId = product.ProductId
        group by ProductName
        order by TotalSales desc
        """
    ).show()
