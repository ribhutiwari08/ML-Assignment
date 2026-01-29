def add_features(X):
    X = X.copy()

    X["mean_radius_area"] = X["mean radius"] * X["mean area"]
    X["texture_smoothness"] = X["mean texture"] / (X["mean smoothness"] + 1e-6)
    X["perimeter_ratio"] = X["mean perimeter"] / (X["mean radius"] + 1e-6)
    X["area_ratio"] = X["mean area"] / (X["mean perimeter"] + 1e-6)

    return X
