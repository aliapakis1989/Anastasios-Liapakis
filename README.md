# Anastasios-Liapakis
PhD Code Anastasios Michael Liapakis/Agricultural University of Athens/Informatics Laboratory
---------------------------------------------------------------------------------------------

At first, open the files: modules.py and Main_code.py.
All the following files must be saved before the running of the program. Please, add the path of the files in lines 15-25 of the Main_code.py.
The files Dictionary_DoQi.txt, Dictionary_DoI.txt and Dictionary_DoS.txt are referred to the designed sentiment dictionaries concerning the Greek F&B domain.
The files LF.txt, LI.txt and LS.txt are referred to the designed lists of aspects concerning the Greek F&B domain.
The file StopWords.txt is referred to the designed StopWords list concerning the Greek F&B domain.
The file negative.txt is referred to the designed list of negations terms concerning the Greek F&B domain.
The files suffix.txt and stemming_exception.txt are referred to the designed list of suffixes concerning the stemming process.
The file kef-2.txt is referred to the designed correlation file concerning the capitalization of the customers' reviews.  
In demo, the annotated data set is used for presenting the proposed hybrid-level of sentiment analysis framework. The main purpose of the designed system is for computing the sentiment orientation of each function in the F&B domain. Thus, the corresponding file is presented as: Annotated1.accdb. Explanations about each field in the database, are presented below:
First field (kleidi): The customers' review ID in the database
Second field (nomos): The name of NUTS3 region that the evaluated company is being operated.
Third field (user): The users' credentials in the e-ordering platform.
Fourth field (Review): The examined customers' reviews.
Fifth field (Date): The reviews' creation date. 
Sixth field (shop): Restaurant's or cafeteria's name.
Seventh field (Stars): Overall evaluation in a 5-Likert scale as was mined from the examined e-ordering platform.
Eigth field (id): The ID of customer's review in the annotated data set.
Ninth field (quality): The system's overall evaluation for the function of food quality.
Tenth field (service): The system's overall evaluation for the function of customer service.
Eleventh field (image): The system's overall evaluation for the function of image of the company. 

