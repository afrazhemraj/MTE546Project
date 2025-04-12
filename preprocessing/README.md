# NCLT Dataset Preprocessing Notebook

This Jupyter notebook (`546preprocessingnotebook.ipynb`) aligns LiDAR scans with ground truth and odometry data from the [NCLT dataset](https://robots.engin.umich.edu/nclt/). The output is a CSV containing filtered and synchronized data for further analysis or model training.

---

## Downloading the Dataset

1. Go to the [NCLT dataset website](https://robots.engin.umich.edu/nclt/).
2. Scroll down to **2013-01-10**.
3. Download the following files:
   - `groundtruth.csv`
   - `sen.tar.gz`
   - `hokuyo.tar.gz`

---

## Preparing the Files

After downloading:

### 1. Extract the files

- From `sen.tar.gz`, extract:
  - `odometry_mu_100hz.csv`

- From `hokuyo.tar.gz`, extract:
  - `hokuyo_30m.bin`

### 2. Convert LiDAR Binary to CSV

Use the provided script [`read_hokuyo_30m.py`] to convert the `.bin` file into `.csv`. To run the script use the following command:

**Command:**
```bash
python read_hokuyo_30m.py hokuyo_30m.bin
```

> **Note:** Make sure `read_hokuyo_30m.py` and `hokuyo_30m.bin` are in the same directory when you run this command. The script will generate `hokuyo_30m.csv`.

---

## Directory Structure

Place the following files inside a folder in your google drive, e.g., `newdataset/`:
```
newdataset/
├── groundtruth.csv
├── odometry_mu_100hz.csv
├── hokuyo_30m.csv   ← output of the Python script
```

---

## How to Run the Notebook

1. Open the notebook in **Google Colab**.
2. Mount your Google Drive by running STEP 1:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

3. Set the path to your folder, update this line of code in STEP 3 to the folder where you included the 3 csv files:
   ```python
   base_path = "/content/drive/MyDrive/newdataset"
   ```

4. Run the notebook from top to bottom:
   - Loads and preprocesses the ground truth, odometry, and LiDAR data.
   - Filters valid LiDAR scans (only 1081 points).
   - Interpolates odometry to ground truth timestamps.
   - Aligns each ground truth timestamp with the closest LiDAR scan.
   - Saves the aligned data to: `aligned_scans_final1.csv`.

---

## Output

- The final file `aligned_scans_final1.csv` will be saved in the same directory as your input files.

---

## Requirements

- Google Colab (or any Python 3+ environment)
- Python packages used:
  - `numpy`
  - `pandas`
  - `scipy`
