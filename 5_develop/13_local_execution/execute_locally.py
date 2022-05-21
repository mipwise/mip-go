import mip_me
import inspect
import os


def _this_directory():
    return os.path.dirname(os.path.realpath(os.path.abspath(inspect.getsourcefile(_this_directory))))


def read_data(input_data, schema):
    print(f'Reading data from: {input_data}')
    path = os.path.join(_this_directory(), "data", input_data)
    assert os.path.exists(path), f"bad path {path}"
    if input_data.endswith("xlsx"):
        return schema.xls.create_pan_dat(path)
    return schema.csv.create_pan_dat(path)


def write_data(sln, output_data, schema):
    print(f'Writing data back to: {output_data}')
    path = os.path.join(_this_directory(), "data", output_data)
    assert os.path.exists(path), f"bad path {path}"
    if output_data.endswith("xlsx"):
        return schema.xls.write_file(sln, path)
    return schema.csv.write_directory(sln, path)


if __name__ == "__main__":
    _input_data = {1: "testing_data_1.xlsx",  # Loads data from the 'data/testing_data_1.xlsx' workbook.
                   2: "testing_data_2",  # Loads data from csv files in the 'data/testing_data_2' directory.
                   3: "inputs"}[1]  # Loads data from csv files in the 'data/inputs' directory.
    engine = {1: 'Action Data Ingestion',
              2: 'Update Food Cost',
              3: 'Main Solve',
              4: 'Report Builder'}[4]
    if engine == 'Action Data Ingestion':
        # Makes a copy of the original data and place it in the 'data/inputs' directory.
        dat = read_data(_input_data, mip_me.input_schema)
        write_data(dat, 'inputs', mip_me.input_schema)
    elif engine == 'Update Food Cost':
        dat = read_data(_input_data, mip_me.input_schema)
        dat = mip_me.action_update_food_cost.update_food_cost_solve(dat)
        write_data(dat, 'inputs', mip_me.input_schema)
    elif engine == 'Main Solve':
        dat = read_data(_input_data, mip_me.input_schema)
        _sln = mip_me.solve(dat)
        write_data(_sln, 'outputs', mip_me.output_schema)
    elif engine == 'Report Builder':
        dat = read_data(_input_data, mip_me.input_schema)
        _sln = read_data('outputs', mip_me.output_schema)
        _sln = mip_me.action_report_builder.report_builder_solve(dat, _sln)
        write_data(_sln, 'outputs', mip_me.output_schema)
    else:
        raise ValueError('Bad engine')

