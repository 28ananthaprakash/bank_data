from flask import Flask, render_template, request, jsonify
#from flask_ngrok import run_with_ngrok
import pandas as pd
import pickle
app = Flask(__name__)
#run_with_ngrok(app)   #starts ngrok when the app is run
model=pickle.load(open('model.pkl','rb'))
@app.route("/")
def hello():
    return render_template('bank.html')

@app.route("/ask", methods=['POST'])
def ask():
  primaryAccountNumber = int(request.form['a'])
  deviceId= int(request.form['b'])
  issuerId= int(request.form['c'])
  DebitCards_Number= int(request.form['d'])
  ZipCode= int(request.form['e'])
  Amount= int(request.form['f'])
  CardExpiryDate= int(request.form['g'])
  CardCvv2Value= int(request.form['h'])
  TransactionId= int(request.form['i'])
  Pan_Number= int(request.form['j'])
  CompanyId= int(request.form['k'])
  BankId= int(request.form['l'])
  TransactionLimits= int(request.form['m'])
  defaultCurrencyIsoCode= int(request.form['n'])
  enterpriseId= int(request.form['o'])
  industryCode= int(request.form['p'])
  businessRegistrationNumber= int(request.form['q'])
  bankAccountNumber= int(request.form['r'])
  taxId= int(request.form['s'])
  Active= int(request.form['t'])
  data1 = [[primaryAccountNumber, deviceId, issuerId, DebitCards_Number, ZipCode, Amount, CardExpiryDate, CardCvv2Value, TransactionId, Pan_Number, CompanyId, BankId, TransactionLimits, defaultCurrencyIsoCode, enterpriseId, industryCode, businessRegistrationNumber, bankAccountNumber, taxId,  Active]]
  #print(data1)
  df = pd.DataFrame(data1,columns =['primaryAccountNumber',
                                    'deviceId',
                                    'issuerId',
                                    'DebitCards Number',
                                    'ZipCode',
                                    'Amount',
                                    'CardExpiryDate',
                                    'CardCvv2Value',
                                    'TransactionId',
                                    'Pan Number',
                                    'CompanyId',
                                    'BankId',
                                    'TransactionLimits',
                                    'companyProfile.defaultCurrencyIsoCode',
                                    'companyProfile.enterpriseId',
                                    'companyProfile.industryCode',
                                    'companyProfile.businessRegistrationNumber',
                                    'companyProfile.bankAccountNumber',
                                    'companyProfile.taxId',
                                    'CompanyProfile Active'])
  #print(df)
  res = model.predict(df)
  #print(res)
  out = "<h1> The result is {}</h1>".format(int(res[0]))
  return out
  #return jsonify({'status':'OK','answer':bot_response})

if __name__ == "__main__":
    app.run()
