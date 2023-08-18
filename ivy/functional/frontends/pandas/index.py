from series import Series
import ivy


class Index:
    def __init__(self, data, dtype=None, copy=False, name=None, tupleize_cols=True):
        self.index = data
        self.index_array = ivy.array(self.index, dtype=dtype)
        self.dtype = dtype
        self.name = name
        self.copy = copy
        self.tupleize_cols = tupleize_cols

    def __repr__(self):
        return f"Index {self.index_array.to_list()}"

    def unique(self, level=None):
        # todo handle level with mutliindexer
        self.index_array = ivy.unique_values(self)
        return Index(self.index_array, dtype=self.dtype, copy=self.copy, name=self.name)

    def is_unique(self):
        uniques = ivy.unique_values(self)
        return len(uniques) == len(self.index_array)

    def to_list(self):
        return self.index_array.to_list()

    def to_numpy(self, dtype=None, copy=False, na_value=ivy.nan, **kwargs):
        if dtype:
            return self.index_array.astype(dtype).to_numpy(copy=copy)
        return self.index_array.to_numpy(copy=copy)

    def to_series(self, index=None, name=None):
        if index is None:
            index = self.index_array
        return Series(index, index=index, name=name)

    def min(self, axis=None, skipna=True, *args, **kwargs):
        if skipna:
            return ivy.nanmin(self.index_array)
        return self.index_array.min()
