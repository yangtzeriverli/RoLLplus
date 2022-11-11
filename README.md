# RoLL: Real-time and Accurate Route Leak Location with Single BGP Update Message

# Background
Route leak has become a serious threat to BGP. RoLL aims to locate route leak in real time and accurately. It is a light weight method that can help AS operator locate route leak AS triplet and take quick response to mitigate it. A random forest model and AS triplet feature realize amaing effect.
## Usage
featureanalysis folder contains AS feature analysis, allsamples.csv is our dataset and you can run 'python3 locator.py' directly to get a result. Preprocessing.py is used for AS triplet extraction from BGP update message.