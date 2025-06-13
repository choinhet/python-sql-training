import duckdb

if __name__ == "__main__":
    duckdb.query(
        """
        select distinct
            Date,
            Value,
            ProductId,
            StoreId
        from read_parquet('../resources/big.parquet')
        order by Date desc
        """
    ).write_parquet('resources/fact_sales.parquet')

    duckdb.query(
        """
        select distinct
            StoreId,
            StoreName,
            State,
            Street,
            Country
        from read_parquet('../resources/big.parquet')
        order by StoreId
        """
    ).write_parquet('resources/dim_store.parquet')

    duckdb.query(
        """
        select distinct
            ProductId,
            ProductName,
            Category,
            Subcategory
        from read_parquet('../resources/big.parquet')
        order by ProductId
        """
    ).write_parquet('resources/dim_product.parquet')
