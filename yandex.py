import datetime

from pandas import json_normalize

input = {
    "UseScoring": True,
    "Premium": 7879.89,
    "AdditionalPremium": 0.0,
    "ProductVersion": "3",
    "ScoringOn": True,
    "ScoringStartDate": None,
    "DateFrom": "2022-06-26T00:00:00",
    "InsSum": 400000.0,
    "Comission": 787.989,
    "ScoringComission": 16.0,
    "PolicyId": "8b6617f5-b5c4-4162-9561-77ca53b472e0",
    "PolicyNumber": "",
    "PrevPolicyId": "029eb9a6-162b-40c1-9e71-1b69a05669df",
    "PrevPolicyNumber": "ХХХ0180376685",
    "InsurerClientType": 1,
    "InsurerBirthDate": "1985-11-10T00:00:00",
    "InsurerDocumentType": 1,
    "InsurerGender": 1,
    "InsurerTitle": "КУКАРЦЕВ ЮРИЙ МИХАЙЛОВИЧ",
    "InsurerPhone": "8(950)273-22-12",
    "DriverMinAge": 34,
    "SellerIKP": "03604",
    "AgentIKP": "03604",
    "VIN": "Z94C241BBJR036070",
    "EnginePower": 123.04,
    "IssueYear": 2017,
    "TSCategory": 2,
    "RegNumber": "Р845КЕ142",
    "BodyNumber": None,
    "ChassisNumber": None,
    "CoefKM": 1.4,
    "CoefKP": 1.0,
    "IsTaxi": False,
    "CoefKO": 1.0,
    "CoefKBM": 0.83,
    "CoefKVC": 1.05,
    "CoefKT": 1.08,
    "BaseRate": 5980.0,
    "CoefKN": 1.0,
    "CoefKPR": 1.0,
    "SeatsNumberTo16": False,
    "MaxWeightTo16": False,
    "CoefKS": 1.0,
    "IsForeignCountry": False,
    "OwnerKLADRCode": "4200700100000",
    "FIASGroup": "2",
    "InsuranceTerm": 12,
    "IsProlongation": False,
    "SavingHour": 16,
    "DateStartAndSavingDateDiff": 6,
    "IsElectronic": False,
    "DriverMinExperience": 4,
    "CurrentSegment": "Целевой-2",
    "PredictSegment": "Целевой-2",
    "TSBrandId": 130,
    "TSBrandName": "Kia",
    "TSBrandRsaCode": "181000000",
    "TSModelId": 2192,
    "TSModelName": "RIO",
    "TSModelRsaCode": "181007204",
    "BKIScore": "",
    "PTSSeries": "",
    "PTSNumber": "",
    "DriverUnlimit": False,
    "AvtoKodJSON": {
        "identifiers": {
            "vehicle": {
                "vin": "Z94C241BBJR036070",
                "reg_num": "Р845КЕ142",
                "sts": "9904449114",
                "pts": "78ОТ823373"
            }
        },
        "tech_data": {
            "brand": {
                "name": {
                    "original": "КИА РИО"
                }
            },
            "type": {
                "name": "Седан"
            },
            "body": {
                "color": {
                    "name": "Оранжевый",
                    "type": "Оранжевый"
                }
            },
            "year": 2017,
            "engine": {
                "fuel": {
                    "type": "Бензиновый",
                    "type_id": "ID_ENGINE_TYPE_PETROL"
                },
                "number": "НW519638",
                "model": {
                    "name": "G4FG"
                },
                "volume": 1591,
                "power": {
                    "hp": 123.04,
                    "kw": 90.5
                }
            },
            "weight": {
                "netto": 1230,
                "max": 1610
            },
            "drive": {
                "type": "Заднеприводной",
                "type_id": "ID_DRIVING_WHEELS_TYPE_REAR"
            },
            "wheel": {
                "position": "LEFT",
                "position_id": "ID_STEERING_WHEEL_TYPE_LEFT"
            }
        },
        "additional_info": {
            "vehicle": {
                "category": {
                    "code": "B"
                },
                "passport": {
                    "date": {
                        "receive": "2017-11-16 00:00:00"
                    },
                    "has_dublicate": False,
                    "number": "78ОТ823373"
                },
                "sts": {
                    "date": {
                        "receive": "2019-01-15 00:00:00"
                    }
                },
                "modifications": {
                    "was_modificated": False
                }
            }
        },
        "registration_actions": {
            "items": [
                {
                    "_id": 2554580916,
                    "date": {
                        "start": "2019-01-15 00:00:00"
                    },
                    "reg_num": "Р845КЕ142",
                    "identifiers": {
                        "pts": "78ОТ823373",
                        "sts": "9904449114"
                    },
                    "owner": {
                        "type": "PERSON"
                    },
                    "type": "Изменение собственника по сделкам, произведенным в любой форме (купля-продажа, дарение, др.) с заменой государственных регистрационных знаков",
                    "geo": {
                        "region": "Кемеровская область",
                        "city": "г Мариинск",
                        "street": "ул 50 лет Октября",
                        "house": "7"
                    }
                },
                {
                    "_id": 2911810579,
                    "date": {
                        "start": "2017-12-27 00:00:00",
                        "end": "2019-01-15 00:00:00"
                    },
                    "reg_num": "У253ЕУ142",
                    "identifiers": {
                        "pts": "78ОТ823373",
                        "sts": "4256824089"
                    },
                    "owner": {
                        "type": "PERSON"
                    },
                    "type": "Первичная регистрация",
                    "geo": {
                        "region": "Кемеровская область",
                        "city": "г Кемерово",
                        "street": "ул Баумана",
                        "house": "14"
                    }
                }
            ],
            "count": 2
        },
        "leasings": {
            "items": [

            ],
            "count": 0,
            "used_in_leasing": False
        },
        "fines": {
            "items": [
                {
                    "_id": 1238423909,
                    "date": {
                        "event": "2020-08-25 00:00:00"
                    },
                    "description": "УИН 32242012200052496001 от 2020-08-25 на 500.00 руб.",
                    "vendor": {
                        "name": "УФК ПО КЕМЕРОВСКОЙ ОБЛАСТИ (ОСП ПО Г. МАРИИНСКУ, МАРИИНСКОМУ И ЧЕБУЛИНСКОМУ РАЙОНАМ УФССП РОССИИ ПО КЕМЕРОВСКОЙ ОБЛАСТИ-КУЗБАССУ Л/С 05391839760)"
                    },
                    "amount": {
                        "value": 500,
                        "total": 500
                    },
                    "discount": {
                        "percent": 50,
                        "date": {
                            "end": "2020-09-14 00:00:00"
                        }
                    },
                    "is_paid": True,
                    "wire": {
                        "user": {
                            "name": "УФК ПО КЕМЕРОВСКОЙ ОБЛАСТИ (ОСП ПО Г. МАРИИНСКУ, МАРИИНСКОМУ И ЧЕБУЛИНСКОМУ РАЙОНАМ УФССП РОССИИ ПО КЕМЕРОВСКОЙ ОБЛАСТИ-КУЗБАССУ Л/С 05391839760)",
                            "tin": "4205077474",
                            "kpp": "421345001"
                        },
                        "bank": {
                            "account": {
                                "number": "40302810800001000033"
                            },
                            "name": "ГРКЦ ГУ БАНКА РОССИИ ПО КЕМЕРОВСКОЙ ОБЛ.",
                            "bik": "043207001"
                        },
                        "okato": "32616101"
                    }
                },
                {
                    "_id": 909826170,
                    "date": {
                        "event": "2020-08-17 00:00:00"
                    },
                    "article": {
                        "code": "12.9ч.2",
                        "description": "Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час"
                    },
                    "description": "УИН 18810142200817004923 от 2020-08-17 на 0.00 руб.",
                    "vendor": {
                        "name": "УФК по Кемеровской области - Кузбассу (Управление МВД России по г. Кемерово, л/с 04391124460)(Центр АФАП ОДД ГИБДД ГУ МВД России по Кемеровской области)"
                    },
                    "amount": {
                        "total": 500
                    },
                    "discount": {
                        "percent": 50,
                        "date": {
                            "end": "2020-09-06 00:00:00"
                        }
                    },
                    "is_paid": True,
                    "wire": {
                        "user": {
                            "name": "УФК по Кемеровской области - Кузбассу (Управление МВД России по г. Кемерово, л/с 04391124460)",
                            "tin": "4207014720",
                            "kpp": "420501001"
                        },
                        "bank": {
                            "account": {
                                "number": "40101810400000010007"
                            },
                            "name": "Отделение Кемерово г. Кемерово",
                            "bik": "043207001"
                        },
                        "payment": {
                            "purpose": "ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810142200817004923"
                        },
                        "kbk": "18811601121010001140",
                        "okato": "32701000"
                    }
                },
                {
                    "_id": 3318051271,
                    "date": {
                        "event": "2020-05-12 00:00:00"
                    },
                    "article": {
                        "code": "12.9ч.2",
                        "description": "Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час"
                    },
                    "description": "УИН 18810142200512040284 от 2020-05-12 на 0.00 руб.",
                    "vendor": {
                        "name": "УФК по Кемеровской области (Управление МВД России по г. Кемерово, л/с 04391124460)(Центр АФАП ОДД ГИБДД ГУ МВД России по Кемеровской области)"
                    },
                    "amount": {
                        "total": 500
                    },
                    "discount": {
                        "percent": 50,
                        "date": {
                            "end": "2020-06-01 00:00:00"
                        }
                    },
                    "is_paid": True,
                    "wire": {
                        "user": {
                            "name": "УФК по Кемеровской области (Управление МВД России по г. Кемерово, л/с 04391124460)",
                            "tin": "4207014720",
                            "kpp": "420501001"
                        },
                        "bank": {
                            "account": {
                                "number": "40101810400000010007"
                            },
                            "name": "Отделение Кемерово г. Кемерово",
                            "bik": "043207001"
                        },
                        "payment": {
                            "purpose": "ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810142200512040284"
                        },
                        "kbk": "18811601121010001140",
                        "okato": "32701000"
                    }
                },
                {
                    "_id": 147029002,
                    "date": {
                        "event": "2020-04-09 00:00:00"
                    },
                    "article": {
                        "code": "12.9ч.2",
                        "description": "Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час"
                    },
                    "description": "УИН 18810142200409015531 от 2020-04-09 на 0.00 руб.",
                    "vendor": {
                        "name": "УФК по Кемеровской области (Управление МВД России по г. Кемерово, л/с 04391124460)(Центр АФАП ОДД ГИБДД ГУ МВД России по Кемеровской области)"
                    },
                    "amount": {
                        "total": 500
                    },
                    "discount": {
                        "percent": 50,
                        "date": {
                            "end": "2020-04-29 00:00:00"
                        }
                    },
                    "is_paid": True,
                    "wire": {
                        "user": {
                            "name": "УФК по Кемеровской области (Управление МВД России по г. Кемерово, л/с 04391124460)",
                            "tin": "4207014720",
                            "kpp": "420501001"
                        },
                        "bank": {
                            "account": {
                                "number": "40101810400000010007"
                            },
                            "name": "Отделение Кемерово г. Кемерово",
                            "bik": "043207001"
                        },
                        "payment": {
                            "purpose": "ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810142200409015531"
                        },
                        "kbk": "18811601121010001140",
                        "okato": "32701000"
                    }
                }
            ],
            "count": 4,
            "has_fines": True
        },
        "taxi": {
            "history": {
                "items": [

                ],
                "count": 0
            },
            "used_in_taxi": False
        },
        "utilizations": {
            "items": [

            ],
            "was_utilized": False,
            "count": 0
        },
        "report_meta": {

        }
    },
    "BKIJSON": None,
    "IsAdditionalAgreement": False,
    "AgentType": 30,
    "FilialCode": "МОС000650",
    "FilialName": "Кемеровский филиал",
    "OwnerRegionName": "Кемеровская область",
    "IsToxic": False,
    "IsMSK": False,
    "IsEGARANT": False,
    "IsEOSAGO": True,
    "IsSold": False,
    "Score": 0.0,
    "SegmentMessage": None,
    "OwnerClientType": 1,
    "TaxiAvtokod": 0,
    "DriversList": [
        {
            "DriverTitle": "КУКАРЦЕВА АНАСТАСИЯ ВЛАДИСЛАВОВНА",
            "DriverGender": 0,
            "DriverAge": 35,
            "DriverExperience": 5
        },
        {
            "DriverTitle": "КУКАРЦЕВ ЮРИЙ МИХАЙЛОВИЧ",
            "DriverGender": 1,
            "DriverAge": 37,
            "DriverExperience": 17
        }
    ],
    "InsurancePeriodList": [
        {
            "DateStart": "2022-06-26T00:00:00",
            "DateEnd": "2023-06-25T23:59:59"
        }
    ],
    "CoefComission": 0,
    "Autocod_Taxi": False,
    "LossRange": 100,
    "MaxLossRange": 100,
    "Region_Equell": 1,
    "TimeStart": "2022-06-20 12-08-03.968943",
    "TimeStartPredict": "2022-06-20 12-08-04.112952",
    "frame_InsurerClientType": 1,
    "frame_DriverMinAge": 34,
    "frame_DriverMinAge_2": 1156,
    "frame_DriverMinExperience": 4,
    "frame_DriverMinExperience_2": 16,
    "frame_Coef_KP": 1.0,
    "frame_Coef_KS": 1.0,
    "frame_CoefKBM": 0.83,
    "frame_DriverUnlimitNum": 0.0,
    "frame_EnginePower+Autocod": 12.0,
    "frame_VehicleAge": 3,
    "frame_OldPolicy_Num": 0,
    "frame_OldClaimSumPol_Num": 0,
    "frame_BKI_scoreNumber_1_Num": 1.0,
    "frame_GenderM": 0,
    "frame_GenderW": 1,
    "frame_Taxi": 0,
    "frame_FIASGroup_Sum_Num": 2.0,
    "frame_OwnerKLADR_Sum_Num": 23.0,
    "frame_TSCategory_Sum_Num": 3.0,
    "frame_TypeFilial_Sum_Num": 3.0,
    "frame_Count_Fine_Speed": 0,
    "frame_Group_Amout_Speed": 0,
    "frame_FIASGroup_Num": 6.0,
    "frame_OwnerKLADR_Num": 5.0,
    "frame_TSCategory_Num": 2.0,
    "frame_TypeFilial_Num": 3.0,
    "frame_Region_Equally": 1,
    "frame_Name": 1,
    "model_ver_poisson": "H2O_v_poisson_fit_Log_BKIFines_without_FIAS_v15",
    "model_ver_gamma": "H2O_v_gamma_fit_Log_BKIFines_without_FIAS_v15",
    "TimeStartToH2O": "2022-06-20 12-08-11.677352",
    "TimeFinishToH2O": "2022-06-20 12-08-11.677352",
    "TimeEndPredict": "2022-06-20 12-08-12.681401",
    "PredictGamma": 84362,
    "PredictPoisson": 0.0299001037090988,
    "MeanLoss": 33.6,
    "new_bts": 5980.0,
    "Test": 1,
    "Autocod_EnginePower": 123.04,
    "FineAvtoKod": 0,
    "amountFineKod": 0,
    "allFine": 4,
    "allAmountFine": 2000,
    "IsRefusal": False,
    "GenderM": 0,
    "GenderW": 1,
    "TimeEnd": "2022-06-20 12-08-12.709404",
    "DriverUnlimitNum": 0.0,
    "EnginePower_Autocod": 12.0,
    "VehicleAge": 3,
    "OldPolicy_Num": 0,
    "OldClaimSumPol_Num": 0,
    "BKI_scoreNumber_1_Num": 1.0,
    "FIASGroup_Sum_Num": 2.0,
    "OwnerKLADR_Sum_Num": 23.0,
    "TSCategory_Sum_Num": 3.0,
    "TypeFilial_Sum_Num": 3.0,
    "Count_Fine_Speed": 0,
    "Group_Amout_Speed": 0,
    "FIASGroup_Num": 6.0,
    "OwnerKLADR_Num": 5.0,
    "TSCategory_Num": 2.0,
    "TypeFilial_Num": 3.0
}

d = {"UseScoring": False, "Premium": 7879.89, "AdditionalPremium": 0.0, "ProductVersion": "3", "ScoringOn": False,
     "ScoringStartDate": None, "DateFrom": "2022-06-26T00:00:00", "InsSum": 400000.0, "Comission": 787.989,
     "ScoringComission": 16.0, "PolicyId": "8b6617f5-b5c4-4162-9561-77ca53b472e0", "PolicyNumber": "",
     "PrevPolicyId": "029eb9a6-162b-40c1-9e71-1b69a05669df", "PrevPolicyNumber": "ХХХ0180376685",
     "InsurerClientType": 1, "InsurerBirthDate": "1985-11-10T00:00:00", "InsurerDocumentType": 1, "InsurerGender": 1,
     "InsurerTitle": "КУКАРЦЕВ ЮРИЙ МИХАЙЛОВИЧ", "InsurerPhone": "8(950)273-22-12", "DriverMinAge": 34,
     "SellerIKP": "03604", "AgentIKP": "03604", "VIN": "Z94C241BBJR036070", "EnginePower": 123.04, "IssueYear": 2017,
     "TSCategory": 2, "RegNumber": "Р845КЕ142", "BodyNumber": None, "ChassisNumber": False, "CoefKM": 1.4,
     "CoefKP": 1.0, "IsTaxi": False, "CoefKO": 1.0, "CoefKBM": 0.83, "CoefKVC": 1.05, "CoefKT": 1.08,
     "BaseRate": 5980.0, "CoefKN": 1.0, "CoefKPR": 1.0, "SeatsNumberTo16": False, "MaxWeightTo16": False, "CoefKS": 1.0,
     "IsForeignCountry": False, "OwnerKLADRCode": "4200700100000", "FIASGroup": "2", "InsuranceTerm": 12,
     "IsProlongation": False, "SavingHour": 16, "DateStartAndSavingDateDiff": 6, "IsElectronic": False,
     "DriverMinExperience": 4, "CurrentSegment": "Целевой-2", "PredictSegment": "Запретительный", "TSBrandId": 130,
     "TSBrandName": "Kia", "TSBrandRsaCode": "181000000", "TSModelId": 2192, "TSModelName": "RIO",
     "TSModelRsaCode": "181007204", "BKIScore": "", "PTSSeries": "", "PTSNumber": "", "DriverUnlimit": False,
     "AvtoKodJSON": {"identifiers": {
         "vehicle": {"vin": "Z94C241BBJR036070", "reg_num": "Р845КЕ142", "sts": "9904449114", "pts": "78ОТ823373"}},
         "tech_data": {"brand": {"name": {"original": "КИА РИО"}}, "type": {"name": "Седан"},
                       "body": {"color": {"name": "Оранжевый", "type": "Оранжевый"}}, "year": 2017,
                       "engine": {"fuel": {"type": "Бензиновый", "type_id": "ID_ENGINE_TYPE_PETROL"},
                                  "number": "НW519638", "model": {"name": "G4FG"}, "volume": 1591,
                                  "power": {"hp": 123.04, "kw": 90.5}},
                       "weight": {"netto": 1230, "max": 1610},
                       "drive": {"type": "Заднеприводной", "type_id": "ID_DRIVING_WHEELS_TYPE_REAR"},
                       "wheel": {"position": "LEFT", "position_id": "ID_STEERING_WHEEL_TYPE_LEFT"}},
         "additional_info": {"vehicle": {"category": {"code": "B"},
                                         "passport": {"date": {"receive": "2017-11-16 00:00:00"},
                                                      "has_dublicate": False, "number": "78ОТ823373"},
                                         "sts": {"date": {"receive": "2019-01-15 00:00:00"}},
                                         "modifications": {"was_modificated": False}}},
         "registration_actions": {"items": [
             {"_id": 2554580916, "date": {"start": "2019-01-15 00:00:00"}, "reg_num": "Р845КЕ142",
              "identifiers": {"pts": "78ОТ823373", "sts": "9904449114"}, "owner": {"type": "PERSON"},
              "type": "Изменение собственника по сделкам, произведенным в любой форме (купля-продажа, дарение, др.) с заменой государственных регистрационных знаков",
              "geo": {"region": "Кемеровская область", "city": "г Мариинск", "street": "ул 50 лет Октября",
                      "house": "7"}},
             {"_id": 2911810579, "date": {"start": "2017-12-27 00:00:00", "end": "2019-01-15 00:00:00"},
              "reg_num": "У253ЕУ142", "identifiers": {"pts": "78ОТ823373", "sts": "4256824089"},
              "owner": {"type": "PERSON"}, "type": "Первичная регистрация",
              "geo": {"region": "Кемеровская область", "city": "г Кемерово", "street": "ул Баумана",
                      "house": "14"}}], "count": 2},
         "leasings": {"items": [], "count": 0, "used_in_leasing": False}, "fines": {"items": [
             {"_id": 1238423909, "date": {"event": "2020-08-25 00:00:00"},
              "description": "УИН 32242012200052496001 от 2020-08-25 на 500.00 руб.", "vendor": {
                 "name": "УФК ПО КЕМЕРОВСКОЙ ОБЛАСТИ (ОСП ПО Г. МАРИИНСКУ, МАРИИНСКОМУ И ЧЕБУЛИНСКОМУ РАЙОНАМ УФССП РОССИИ ПО КЕМЕРОВСКОЙ ОБЛАСТИ-КУЗБАССУ Л/С 05391839760)"},
              "amount": {"value": 500, "total": 500},
              "discount": {"percent": 50, "date": {"end": "2020-09-14 00:00:00"}}, "is_paid": False, "wire": {"user": {
                 "name": "УФК ПО КЕМЕРОВСКОЙ ОБЛАСТИ (ОСП ПО Г. МАРИИНСКУ, МАРИИНСКОМУ И ЧЕБУЛИНСКОМУ РАЙОНАМ УФССП РОССИИ ПО КЕМЕРОВСКОЙ ОБЛАСТИ-КУЗБАССУ Л/С 05391839760)",
                 "tin": "4205077474", "kpp": "421345001"}, "bank": {"account": {"number": "40302810800001000033"},
                                                                    "name": "ГРКЦ ГУ БАНКА РОССИИ ПО КЕМЕРОВСКОЙ ОБЛ.",
                                                                    "bik": "043207001"}, "okato": "32616101"}},
             {"_id": 909826170, "date": {"event": "2020-08-17 00:00:00"}, "article": {"code": "12.9ч.2",
                                                                                      "description": "Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час"},
              "description": "УИН 18810142200817004923 от 2020-08-17 на 0.00 руб.", "vendor": {
                 "name": "УФК по Кемеровской области - Кузбассу (Управление МВД России по г. Кемерово, л/с 04391124460)(Центр АФАП ОДД ГИБДД ГУ МВД России по Кемеровской области)"},
              "amount": {"total": 500}, "discount": {"percent": 50, "date": {"end": "2020-09-06 00:00:00"}},
              "is_paid": False, "wire": {"user": {
                 "name": "УФК по Кемеровской области - Кузбассу (Управление МВД России по г. Кемерово, л/с 04391124460)",
                 "tin": "4207014720", "kpp": "420501001"}, "bank": {"account": {"number": "40101810400000010007"},
                                                                    "name": "Отделение Кемерово г. Кемерово",
                                                                    "bik": "043207001"}, "payment": {
                 "purpose": "ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810142200817004923"},
                 "kbk": "18811601121010001140", "okato": "32701000"}},
             {"_id": 3318051271, "date": {"event": "2020-05-12 00:00:00"}, "article": {"code": "12.9ч.2",
                                                                                       "description": "Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час"},
              "description": "УИН 18810142200512040284 от 2020-05-12 на 0.00 руб.", "vendor": {
                 "name": "УФК по Кемеровской области (Управление МВД России по г. Кемерово, л/с 04391124460)(Центр АФАП ОДД ГИБДД ГУ МВД России по Кемеровской области)"},
              "amount": {"total": 500}, "discount": {"percent": 50, "date": {"end": "2020-06-01 00:00:00"}},
              "is_paid": False, "wire": {
                 "user": {"name": "УФК по Кемеровской области (Управление МВД России по г. Кемерово, л/с 04391124460)",
                          "tin": "4207014720", "kpp": "420501001"},
                 "bank": {"account": {"number": "40101810400000010007"}, "name": "Отделение Кемерово г. Кемерово",
                          "bik": "043207001"}, "payment": {
                     "purpose": "ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810142200512040284"},
                 "kbk": "18811601121010001140", "okato": "32701000"}},
             {"_id": 147029002, "date": {"event": "2020-04-09 00:00:00"}, "article": {"code": "12.9ч.2",
                                                                                      "description": "Превышение установленной скорости движения транспортного средства на величину более 20, но не более 40 километров в час"},
              "description": "УИН 18810142200409015531 от 2020-04-09 на 0.00 руб.", "vendor": {
                 "name": "УФК по Кемеровской области (Управление МВД России по г. Кемерово, л/с 04391124460)(Центр АФАП ОДД ГИБДД ГУ МВД России по Кемеровской области)"},
              "amount": {"total": 500}, "discount": {"percent": 50, "date": {"end": "2020-04-29 00:00:00"}},
              "is_paid": False, "wire": {
                 "user": {"name": "УФК по Кемеровской области (Управление МВД России по г. Кемерово, л/с 04391124460)",
                          "tin": "4207014720", "kpp": "420501001"},
                 "bank": {"account": {"number": "40101810400000010007"}, "name": "Отделение Кемерово г. Кемерово",
                          "bik": "043207001"}, "payment": {
                     "purpose": "ШТРАФ ПО АДМИНИСТРАТИВНОМУ ПРАВОНАРУШЕНИЮ ПОСТАНОВЛЕНИЕ №18810142200409015531"},
                 "kbk": "18811601121010001140", "okato": "32701000"}}], "count": 4, "has_fines": False},
         "taxi": {"history": {"items": [], "count": 0}, "used_in_taxi": False},
         "utilizations": {"items": [], "was_utilized": False, "count": 0}, "report_meta": {}},
     "BKIJSON": None, "IsAdditionalAgreement": False, "AgentType": 30, "FilialCode": "МОС000650",
     "FilialName": "Кемеровский филиал", "OwnerRegionName": "Кемеровская область", "IsToxic": False, "IsMSK": False,
     "IsEGARANT": False, "IsEOSAGO": False, "IsSold": False, "Score": 0.0, "SegmentMessage": None, "OwnerClientType": 1,
     "TaxiAvtokod": 0, "DriversList": [
        {"DriverTitle": "КУКАРЦЕВА АНАСТАСИЯ ВЛАДИСЛАВОВНА", "DriverGender": 0, "DriverAge": 35, "DriverExperience": 5},
        {"DriverTitle": "КУКАРЦЕВ ЮРИЙ МИХАЙЛОВИЧ", "DriverGender": 1, "DriverAge": 37, "DriverExperience": 17}],
     "InsurancePeriodList": [{"DateStart": "2022-06-26T00:00:00", "DateEnd": "2023-06-25T23:59:59"}],
     "now_date": "2022-06-20 12-08-03.974249", "Autocod_year": 2017, "Autocod_EnginePower": 123.04,
     "Autocod_Taxi": False, "frame_GenderM": 0, "frame_GenderW": 1, "frame_IsGoodName": 0, "frame_DriverMinAge": 34,
     "frame_DriverMinAge_M": 18, "frame_DriverMinAge_M_2": 324, "frame_DriverMinAge_W": 34,
     "frame_DriverMinAge_W_2": 1156, "frame_DriverMinExperience": 4, "frame_DriverMinExperience_2": 16,
     "frame_DriverLicenseAge": 30, "frame_CoefKVC": 10, "frame_CoefKBM": 8, "frame_kbm_exp10plus": 1,
     "frame_kbm_exp10minus": 8, "frame_kbm_exp10plus_2": 1, "frame_kbm_exp10minus_2": 64, "frame_kvc_kbm": 9,
     "frame_veh_moto": 0, "frame_veh_car": 1, "frame_veh_truck": 0, "frame_VehicleAge": 5, "frame_VehicleAge_2": 25,
     "frame_EnginePower": 12, "frame_SeatsNumberTo16": 0, "frame_MaxWeightTo16": 0, "frame_OwnerKLADRCode_2": "42",
     "frame_OwnerKLADR_Num": 15.0, "frame_freq_geo": 0.040873550822, "frame_freq_0_100_geo": 0.032030196818,
     "frame_freq_100_geo": 0.008843354003, "frame_population_50": 52550.0, "frame_population_1000": 0,
     "frame_population_500": 0, "frame_population_250": 0, "frame_population_60": 0,
     "frame_city_population_max_50": 38210.0, "frame_city_dist_max_50": 1.3714979145765929,
     "frame_center_population": 558662.0, "frame_center_dist": 139.614190224471,
     "frame_region_density": 28.4668581875163, "frame_population_50_log": 10.869520376305097,
     "frame_city_population_max_50_log": 10.550852540440946, "frame_city_dist_max_50_log": 0.3159035108523254,
     "frame_center_population_log": 13.23329991809921, "frame_center_dist_log": 4.938882834334773,
     "frame_region_density_log": 3.3487405400024812, "LossRange": 100, "MaxLossRange": 100,
     "now_date_end": "2022-06-20 12-08-03.989872"}

import json
import pandas as pd

b = json.loads(json.dumps(d))
df = pd.DataFrame([b], columns=b.keys())


pd.set_option('display.max_columns', 100)



df['AvtoKodJSON'] = df['AvtoKodJSON'].astype(str)
df['DriversList'] = df['DriversList'].astype(str)
df['InsurancePeriodList'] = df['InsurancePeriodList'].astype(str)

import sqlite3

#
con = sqlite3.connect('sqlite.db')
import time

start = time.time()

df.to_sql(name='osago1', con=con, if_exists='append')

done = time.time()
elapsed = done - start
print(elapsed)
