import duckdb

if __name__ == "__main__":
    duckdb.query(
        """
        select *
        from read_parquet('resources/big.parquet')
        """
    ).write_parquet('resources/bad.parquet')
