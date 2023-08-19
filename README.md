# Dataset Augmentation and Labeling Toolkit

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Crop Main Classes](#crop-main-classes)
  - [Crop All Characters](#crop-all-characters)
  - [Combine and Transform Datasets](#combine-and-transform-datasets)
  - [Delete Unlabeled Images](#delete-unlabeled-images)
  - [Filter Small Images](#filter-small-images)
  - [Balancing and Augmenting Data](#balancing-and-augmenting-data)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Dataset Augmentation and Labeling Toolkit is a collection of Python scripts designed to assist you in managing and enhancing your image datasets for machine learning projects, particularly those used with YOLO labeling.

## Features

- **Crop Main Classes**: Use `crop_only_plate_with_its_labels.py` to crop the primary class containing data from images. The result is organized into folders with class names.

- **Crop All Characters**: Utilize `crop_all_charachter_in_dataset.py` to crop all classes in each photo and label each image with a single class, enabling dataset augmentation.

- **Combine and Transform Datasets**: If you have multiple datasets with different class names, employ `change_all_dataset_to_its_name_from_data_yaml.py` to standardize class names. Revert to class index numbers with `replace_class_name_with_its_index.py` as needed.

- **Remove Specific Class**: Use `remove_specific_class.py` to delete specific classes from your dataset.

- **Delete Unlabeled Images**: Remove unlabeled images from your dataset using `delete_the_not_labeled_images.py`.

- **Filter Small Images**: Eliminate small images from the crop folder with `delete_all_images_under_800_size.py`, ensuring high-quality data.

- **Balancing and Augmenting Data**: The `balance_data.py` script enables you to balance class sizes and augment your dataset. You can adjust the maximum number of instances per class to suit your needs, creating larger datasets with various augmentation options for improved model accuracy.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries (dependencies listed in individual scripts)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/dataset-augmentation-toolkit.git
   cd dataset-augmentation-toolkit
