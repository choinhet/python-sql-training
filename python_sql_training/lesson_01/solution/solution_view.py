import duckdb

if __name__ == "__main__":
    duckdb.query(
        """
        select *
        from read_parquet('resources/fact_sales.parquet')
        """
    ).show()

    duckdb.query(
        """
        select *
        from read_parquet('resources/dim_product.parquet')
        """
    ).show()

    duckdb.query(
        """
        select *
        from read_parquet('resources/dim_store.parquet')
        """
    ).show()