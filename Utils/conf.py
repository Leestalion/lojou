######## ALL PATH
path_pipeline_obj = r'./finalized_pipeline.pkl'
path_lime_explainer = r'./lime_explainer.pkl'
path_train = r'./input/df_train_sample.csv'
path_test = r'./input/df_test_sample.csv'

######## PARAMETER
threshold = 0.325
col_for_explaination = ['CNT_CHILDREN', 'AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY',
       'DAYS_BIRTH', 'DAYS_EMPLOYED', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH',
       'HOUR_APPR_PROCESS_START', 'EXT_SOURCE_2',
       'EXT_SOURCE_3', 'DAYS_LAST_PHONE_CHANGE', 'AMT_REQ_CREDIT_BUREAU_WEEK',
       'AMT_REQ_CREDIT_BUREAU_MON', 'AMT_REQ_CREDIT_BUREAU_QRT',
       'AMT_REQ_CREDIT_BUREAU_YEAR', 'INCOME_CREDIT_PERC',
       'BURO_DAYS_CREDIT_MIN', 'BURO_DAYS_CREDIT_MAX', 'BURO_DAYS_CREDIT_MEAN',
       'BURO_DAYS_CREDIT_VAR', 'BURO_DAYS_CREDIT_ENDDATE_MIN',
       'BURO_DAYS_CREDIT_ENDDATE_MAX', 'BURO_DAYS_CREDIT_ENDDATE_MEAN',
       'BURO_DAYS_CREDIT_UPDATE_MEAN', 'BURO_AMT_CREDIT_SUM_MAX',
       'BURO_AMT_CREDIT_SUM_MEAN', 'BURO_AMT_CREDIT_SUM_SUM',
       'BURO_AMT_CREDIT_SUM_DEBT_MAX', 'BURO_AMT_CREDIT_SUM_DEBT_MEAN',
       'BURO_AMT_CREDIT_SUM_OVERDUE_MEAN', 'BURO_AMT_CREDIT_SUM_LIMIT_MEAN',
       'BURO_AMT_CREDIT_SUM_LIMIT_SUM', 'BURO_CNT_CREDIT_PROLONG_SUM',
       'BURO_MONTHS_BALANCE_SIZE_SUM', 'BURO_CREDIT_ACTIVE_Active_MEAN',
       'BURO_CREDIT_TYPE_Consumer credit_MEAN', 'ACTIVE_DAYS_CREDIT_MIN',
       'ACTIVE_DAYS_CREDIT_UPDATE_MEAN', 'ACTIVE_AMT_CREDIT_SUM_MEAN',
       'ACTIVE_AMT_CREDIT_SUM_OVERDUE_MEAN', 'ACTIVE_CNT_CREDIT_PROLONG_SUM',
       'ACTIVE_MONTHS_BALANCE_SIZE_SUM','CLOSED_AMT_CREDIT_SUM_MAX', 'CLOSED_AMT_CREDIT_SUM_SUM',
       'CLOSED_AMT_CREDIT_SUM_DEBT_MAX', 'CLOSED_AMT_CREDIT_SUM_DEBT_MEAN',
       'CLOSED_AMT_CREDIT_SUM_OVERDUE_MEAN', 'CLOSED_AMT_CREDIT_SUM_LIMIT_SUM',
       'PREV_AMT_ANNUITY_MIN', 'PREV_AMT_ANNUITY_MAX', 'PREV_AMT_ANNUITY_MEAN',
       'PREV_AMT_APPLICATION_MIN', 'PREV_AMT_APPLICATION_MAX',
       'PREV_AMT_APPLICATION_MEAN', 'PREV_APP_CREDIT_PERC_MIN',
       'PREV_APP_CREDIT_PERC_MAX', 'PREV_APP_CREDIT_PERC_MEAN',
       'PREV_APP_CREDIT_PERC_VAR', 'PREV_AMT_DOWN_PAYMENT_MIN',
       'PREV_AMT_DOWN_PAYMENT_MAX', 'PREV_AMT_GOODS_PRICE_MIN',
       'PREV_HOUR_APPR_PROCESS_START_MIN', 'PREV_HOUR_APPR_PROCESS_START_MAX',
       'PREV_DAYS_DECISION_MIN', 'PREV_DAYS_DECISION_MAX',
       'PREV_DAYS_DECISION_MEAN', 'PREV_CNT_PAYMENT_MEAN',
       'PREV_CNT_PAYMENT_SUM']