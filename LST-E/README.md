---
license: mit
language:
- en
inference: false
datasets:
- scalytics/smartmeterdata
---

**Owner:** Scalytics, Inc.   
**Blogpost:** [Democratizing neuronal networks to predict energy consumption](https://www.databloom.ai/blog/democratizing-neuronal-networks-to-predict-energy-consumption) 

### Model Overview ###
LST-E [last energy] is a Long short-term memory model to predict energy consumption forecasts based on historical data. It basically takes 
some smartmeter data (5 cols, > 12mil. instances, cols: id, device_name, property, value, timestamp) and creates a custom forecast based on selected window. 

Please notice that once you load up the smartmeter data, there are inputs created on the timestamp col like wd_input (the weekday of the timestamp), as well as a cos(inus) and sin(us)
time inputs, giving the model the ability to keep track of the daytime of each instance. Finally, the inputs are merged into an input df, standardized, and differenced.
After that, some functions are used to give the user the ability to use time windows from the data. Based on these, the model generates forecasts.
   
![Model](https://github.com/scalytics/LSTM-NNW/blob/main/LST-E/model.png)
   
The first models created are a simple baseline model, used for evaluating the performance of the later on built LSTM model. The baseline model simply shifts the values by t=1. Hence,
there is no t=0 and each timestamp uses the value from t-1.
Finally, there's the 2-layer plain vanilla LSTM. After 11 epochs, I reached a loss of 10.86. The main idea here is to build a basic forecasting model for which this seems appropriate.   

![LTSM](https://github.com/scalytics/LSTM-NNW/blob/main/LST-E/lstm.png)

***Happy Hacking!***