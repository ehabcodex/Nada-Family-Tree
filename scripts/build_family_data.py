# -*- coding: utf-8 -*-
"""
Builder and validator for Al-Nada family tree dataset
"""
import json
import os

def get_complete_tree():
    return {
        "id": "root_al_nada",
        "name_ar": "آل ندى",
        "name_en": "Al-Nada Family",
        "generation": 0,
        "branch_ar": "الأصل",
        "branch_en": "Root",
        "notes": "",
        "children": [
            {
                "id": "mustafa_1",
                "name_ar": "مصطفى",
                "name_en": "Mustafa (I)",
                "generation": 1,
                "branch_ar": "الجد المؤسس",
                "branch_en": "Founding Ancestor",
                "notes": "",
                "children": [
                    {
                        "id": "hamad_1",
                        "name_ar": "حمد",
                        "name_en": "Hamad",
                        "generation": 2,
                        "branch_ar": "الجد الجامع",
                        "branch_en": "Common Ancestor",
                        "notes": "",
                        "children": [
                            # =========================================================================
                            # Branch 1: مصطفى بن حمد
                            # =========================================================================
                            {
                                "id": "mustafa_hamad",
                                "name_ar": "مصطفى",
                                "name_en": "Mustafa (bin Hamad)",
                                "generation": 3,
                                "branch_ar": "فرع مصطفى بن حمد",
                                "branch_en": "Mustafa bin Hamad Branch",
                                "notes": "",
                                "children": [
                                    # 1.1 محمود بن مصطفى
                                    {
                                        "id": "mahmoud_mustafa",
                                        "name_ar": "محمود",
                                        "name_en": "Mahmoud",
                                        "generation": 4,
                                        "branch_ar": "فرع محمود بن مصطفى",
                                        "branch_en": "Mahmoud bin Mustafa Branch",
                                        "notes": "",
                                        "children": [
                                            {
                                                "id": "mohd_mahmoud",
                                                "name_ar": "محمد",
                                                "name_en": "Muhammad",
                                                "generation": 5,
                                                "children": [
                                                    {
                                                        "id": "ahmad_mohd_mahmoud",
                                                        "name_ar": "احمد",
                                                        "name_en": "Ahmad",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "yasser_ahmad_m",
                                                                "name_ar": "ياسر",
                                                                "name_en": "Yasser",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "muath_yasser", "name_ar": "معاذ", "name_en": "Muath", "generation": 8, "children": []},
                                                                    {"id": "zaid_yasser", "name_ar": "زيد", "name_en": "Zaid", "generation": 8, "children": []},
                                                                    {"id": "ahmad_yasser", "name_ar": "احمد", "name_en": "Ahmad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "mohd_ahmad_m",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "hussein_mohd_a", "name_ar": "حسين", "name_en": "Hussein", "generation": 8, "children": []},
                                                                    {"id": "mohd_mohd_a", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "mustafa_mohd_a", "name_ar": "مصطفي", "name_en": "Mustafa", "generation": 8, "children": []},
                                                                    {"id": "youssef_mohd_a", "name_ar": "يوسف", "name_en": "Youssef", "generation": 8, "children": []},
                                                                    {"id": "mahmoud_mohd_a", "name_ar": "محمود", "name_en": "Mahmoud", "generation": 8, "children": []},
                                                                    {"id": "anas_mohd_a", "name_ar": "انس", "name_en": "Anas", "generation": 8, "children": []},
                                                                    {"id": "bilal_mohd_a", "name_ar": "بلال", "name_en": "Bilal", "generation": 8, "children": []},
                                                                    {"id": "ali_mohd_a", "name_ar": "علي", "name_en": "Ali", "generation": 8, "children": []},
                                                                    {"id": "sanad_mohd_a", "name_ar": "سند", "name_en": "Sanad", "generation": 8, "children": []},
                                                                    {"id": "wisam_mohd_a", "name_ar": "وسام", "name_en": "Wissam", "generation": 8, "children": []},
                                                                    {"id": "waseem_mohd_a", "name_ar": "وسيم", "name_en": "Waseem", "generation": 8, "children": []},
                                                                    {"id": "hamza_mohd_a", "name_ar": "حمزة", "name_en": "Hamza", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "nasser_ahmad_m", "name_ar": "ناصر", "name_en": "Nasser", "generation": 7, "children": []},
                                                            {"id": "mahmoud_ahmad_m", "name_ar": "محمود", "name_en": "Mahmoud", "generation": 7, "children": []},
                                                            {"id": "issam_ahmad_m", "name_ar": "عصام", "name_en": "Issam", "generation": 7, "children": []},
                                                            {"id": "iyad_ahmad_m", "name_ar": "اياد", "name_en": "Iyad", "generation": 7, "children": []},
                                                            {"id": "motasem_ahmad_m", "name_ar": "معتصم", "name_en": "Moatasem", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "sami_mohd_m",
                                                        "name_ar": "سامي",
                                                        "name_en": "Sami",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "ahmad_sami", "name_ar": "احمد", "name_en": "Ahmad", "generation": 7, "children": []},
                                                            {"id": "mohd_sami", "name_ar": "محمد", "name_en": "Muhammad", "generation": 7, "children": []},
                                                            {"id": "walid_sami", "name_ar": "وليد", "name_en": "Walid", "generation": 7, "children": []},
                                                            {"id": "khaled_sami", "name_ar": "خالد", "name_en": "Khaled", "generation": 7, "children": []},
                                                            {"id": "mahmoud_sami", "name_ar": "محمود", "name_en": "Mahmoud", "generation": 7, "children": []},
                                                            {"id": "mufid_sami", "name_ar": "مفيد", "name_en": "Mufeed", "generation": 7, "children": []}
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "abdelhamid_mahmoud",
                                                "name_ar": "عبد الحميد",
                                                "name_en": "Abdel Hamid",
                                                "generation": 5,
                                                "children": [
                                                    {
                                                        "id": "naeim_abdelhamid",
                                                        "name_ar": "نعيم",
                                                        "name_en": "Naeem",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "nasser_naeim",
                                                                "name_ar": "ناصر",
                                                                "name_en": "Nasser",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "tamer_nasser", "name_ar": "تامر", "name_en": "Tamer", "generation": 8, "children": []},
                                                                    {"id": "hamza_nasser", "name_ar": "حمزة", "name_en": "Hamza", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "bassam_naeim",
                                                                "name_ar": "بسام",
                                                                "name_en": "Bassam",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "kareem_bassam", "name_ar": "كريم", "name_en": "Kareem", "generation": 8, "children": []},
                                                                    {"id": "ameer_bassam", "name_ar": "امير", "name_en": "Ameer", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "mohd_naeim",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "mohd_mohd_naeim", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "ghassan_naeim",
                                                                "name_ar": "غسان",
                                                                "name_en": "Ghassan",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "momen_ghassan", "name_ar": "مؤمن", "name_en": "Moamen", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "abdelhakeem_naeim",
                                                                "name_ar": "عبد الحكيم",
                                                                "name_en": "Abdel Hakeem",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "mahmoud_abdelhakeem", "name_ar": "محمود", "name_en": "Mahmoud", "generation": 8, "children": []},
                                                                    {"id": "mohd_abdelhakeem", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "ahmad_abdelhakeem", "name_ar": "احمد", "name_en": "Ahmad", "generation": 8, "children": []},
                                                                    {"id": "huthayfa_abdelhakeem", "name_ar": "حذيفة", "name_en": "Huthaifa", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "id": "abdullah_abdelhamid",
                                                        "name_ar": "عبد اللة",
                                                        "name_en": "Abdullah",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "osama_abdullah",
                                                                "name_ar": "اسامة",
                                                                "name_en": "Osama",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "abdullah_osama", "name_ar": "عبدالله", "name_en": "Abdullah", "generation": 8, "children": []},
                                                                    {"id": "mohd_osama", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "obada_osama", "name_ar": "عبادة", "name_en": "Obada", "generation": 8, "children": []},
                                                                    {"id": "zain_osama", "name_ar": "زين", "name_en": "Zain", "generation": 8, "children": []},
                                                                    {"id": "seraj_osama", "name_ar": "سراج", "name_en": "Seraj", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "ahmad_abdullah",
                                                                "name_ar": "احمد",
                                                                "name_en": "Ahmad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "yamen_ahmad", "name_ar": "يامن", "name_en": "Yamen", "generation": 8, "children": []},
                                                                    {"id": "abdelrahman_ahmad", "name_ar": "عبد الرحمن", "name_en": "Abdel Rahman", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "mohd_abdullah",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "zaid_mohd_abd", "name_ar": "زيد", "name_en": "Zaid", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "ibrahim_abdullah",
                                                                "name_ar": "ابراهيم",
                                                                "name_en": "Ibrahim",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "omar_ibrahim_abd", "name_ar": "عمر", "name_en": "Omar", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "mahmoud_abdullah", "name_ar": "محمود", "name_en": "Mahmoud", "generation": 7, "children": []},
                                                            {"id": "abdelhamid_abdullah", "name_ar": "عبد الحميد", "name_en": "Abdel Hamid", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "saeed_abdelhamid",
                                                        "name_ar": "سعيد",
                                                        "name_en": "Saeed",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "ziad_saeed",
                                                                "name_ar": "زياد",
                                                                "name_en": "Ziad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "mohd_ziad", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "ibrahim_ziad", "name_ar": "ابراهيم", "name_en": "Ibrahim", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "emad_saeed",
                                                                "name_ar": "عماد",
                                                                "name_en": "Emad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "ehab_emad", "name_ar": "ايهاب", "name_en": "Ihab", "generation": 8, "children": []},
                                                                    {"id": "mohd_emad", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "raed_saeed",
                                                                "name_ar": "رائد",
                                                                "name_en": "Raed",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "saeed_raed", "name_ar": "سعيد", "name_en": "Saeed", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "issam_saeed",
                                                                "name_ar": "عصام",
                                                                "name_en": "Issam",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "diaa_issam", "name_ar": "ضياء", "name_en": "Diaa", "generation": 8, "children": []},
                                                                    {"id": "zakaria_issam", "name_ar": "زكريا", "name_en": "Zakaria", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    # 1.2 احمد بن مصطفى
                                    {
                                        "id": "ahmad_mustafa",
                                        "name_ar": "احمد",
                                        "name_en": "Ahmad",
                                        "generation": 4,
                                        "branch_ar": "فرع احمد بن مصطفى",
                                        "branch_en": "Ahmad bin Mustafa Branch",
                                        "notes": "",
                                        "children": [
                                            {
                                                "id": "hafiz_ahmad",
                                                "name_ar": "حافظ",
                                                "name_en": "Hafiz",
                                                "generation": 5,
                                                "children": [
                                                    {
                                                        "id": "fakhri_hafiz",
                                                        "name_ar": "فخري",
                                                        "name_en": "Fakhri",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "youssef_fakhri", "name_ar": "يوسف", "name_en": "Youssef", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "jehad_hafiz",
                                                        "name_ar": "جهاد",
                                                        "name_en": "Jehad",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "mohd_jehad",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "moawia_mohd_j", "name_ar": "معاوية", "name_en": "Moawiya", "generation": 8, "children": []},
                                                                    {"id": "zaid_mohd_j", "name_ar": "زيد", "name_en": "Zaid", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "mahmoud_jehad",
                                                                "name_ar": "محمود",
                                                                "name_en": "Mahmoud",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "jehad_mahmoud_j", "name_ar": "جهاد", "name_en": "Jehad", "generation": 8, "children": []},
                                                                    {"id": "wisam_mahmoud_j", "name_ar": "وسام", "name_en": "Wissam", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "ahmad_jehad",
                                                                "name_ar": "احمد",
                                                                "name_en": "Ahmad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "motasem_ahmad_j", "name_ar": "معتصم", "name_en": "Moatasem", "generation": 8, "children": []},
                                                                    {"id": "moataz_ahmad_j", "name_ar": "معتز", "name_en": "Moataz", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "abdelkareem_jehad",
                                                                "name_ar": "عبد الكريم",
                                                                "name_en": "Abdel Kareem",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "majd_abdelkareem", "name_ar": "مجد", "name_en": "Majd", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "abbas_ahmad",
                                                "name_ar": "عباس",
                                                "name_en": "Abbas",
                                                "generation": 5,
                                                "children": [
                                                    {
                                                        "id": "rushdi_abbas",
                                                        "name_ar": "رشدي",
                                                        "name_en": "Rushdi",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "youssef_rushdi",
                                                                "name_ar": "يوسف",
                                                                "name_en": "Youssef",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "ammar_youssef_r",
                                                                        "name_ar": "عمار",
                                                                        "name_en": "Ammar",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "youssef_ammar", "name_ar": "يوسف", "name_en": "Youssef", "generation": 9, "children": []},
                                                                            {"id": "abdullah_ammar", "name_ar": "عبدالله", "name_en": "Abdullah", "generation": 9, "children": []},
                                                                            {"id": "zaid_ammar", "name_ar": "زيد", "name_en": "Zaid", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {
                                                                        "id": "khaled_youssef_r",
                                                                        "name_ar": "خالد",
                                                                        "name_en": "Khaled",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "ahmad_khaled_yr", "name_ar": "احمد", "name_en": "Ahmad", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {
                                                                        "id": "issam_youssef_r",
                                                                        "name_ar": "عصام",
                                                                        "name_en": "Issam",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "yazan_issam_yr", "name_ar": "يزن", "name_en": "Yazan", "generation": 9, "children": []},
                                                                            {"id": "abdelrahman_issam_yr", "name_ar": "عبد الرحمن", "name_en": "Abdel Rahman", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {"id": "ahmad_youssef_r", "name_ar": "احمد", "name_en": "Ahmad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "mohd_rushdi",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "rami_mohd_r",
                                                                        "name_ar": "رامي",
                                                                        "name_en": "Rami",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "mohd_rami_r", "name_ar": "محمد", "name_en": "Muhammad", "generation": 9, "children": []},
                                                                            {"id": "ahmad_rami_r", "name_ar": "احمد", "name_en": "Ahmad", "generation": 9, "children": []},
                                                                            {"id": "qais_rami_r", "name_ar": "قيس", "name_en": "Qais", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {
                                                                        "id": "yasser_mohd_r",
                                                                        "name_ar": "ياسر",
                                                                        "name_en": "Yasser",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "jehad_yasser_r", "name_ar": "جهاد", "name_en": "Jehad", "generation": 9, "children": []}
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "id": "hafiz_rushdi",
                                                                "name_ar": "حافظ",
                                                                "name_en": "Hafiz",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "nasser_hafiz_r", "name_ar": "ناصر", "name_en": "Nasser", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "ibrahim_rushdi",
                                                                "name_ar": "ابراهيم",
                                                                "name_en": "Ibrahim",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "khalil_ibrahim_r",
                                                                        "name_ar": "خليل",
                                                                        "name_en": "Khalil",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "ali_khalil_ir", "name_ar": "علي", "name_en": "Ali", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {
                                                                        "id": "rushdi_ibrahim_r",
                                                                        "name_ar": "رشدي",
                                                                        "name_en": "Rushdi",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "hamza_rushdi_ir", "name_ar": "حمزة", "name_en": "Hamza", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {"id": "abbas_ibrahim_r", "name_ar": "عباس", "name_en": "Abbas", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "saleh_rushdi",
                                                                "name_ar": "صالح",
                                                                "name_en": "Saleh",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "shalash_saleh_r", "name_ar": "شلاش", "name_en": "Shalash", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "hatem_rushdi", "name_ar": "حاتم", "name_en": "Hatem", "generation": 7, "children": []},
                                                            {
                                                                "id": "tawfiq_rushdi",
                                                                "name_ar": "توفيق",
                                                                "name_en": "Tawfiq",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "rushdi_tawfiq",
                                                                        "name_ar": "رشدي",
                                                                        "name_en": "Rushdi",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "mohd_rushdi_t", "name_ar": "محمد", "name_en": "Muhammad", "generation": 9, "children": []},
                                                                            {"id": "abdelrahman_rushdi_t", "name_ar": "عبد الرحمن", "name_en": "Abdel Rahman", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {"id": "mahmoud_tawfiq", "name_ar": "محمود", "name_en": "Mahmoud", "generation": 8, "children": []},
                                                                    {"id": "mohd_tawfiq", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {
                                                                        "id": "abbas_tawfiq",
                                                                        "name_ar": "عباس",
                                                                        "name_en": "Abbas",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "mohd_abbas_t", "name_ar": "محمد", "name_en": "Muhammad", "generation": 9, "children": []},
                                                                            {"id": "abdullah_abbas_t", "name_ar": "عبدالله", "name_en": "Abdullah", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {"id": "ahmad_tawfiq", "name_ar": "احمد", "name_en": "Ahmad", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            },
                            # =========================================================================
                            # Branch 2: علي بن حمد
                            # =========================================================================
                            {
                                "id": "ali_hamad",
                                "name_ar": "علي",
                                "name_en": "Ali (bin Hamad)",
                                "generation": 3,
                                "branch_ar": "فرع علي بن حمد",
                                "branch_en": "Ali bin Hamad Branch",
                                "notes": "",
                                "children": [
                                    # 2.1 صالح بن علي
                                    {
                                        "id": "saleh_ali",
                                        "name_ar": "صالح",
                                        "name_en": "Saleh",
                                        "generation": 4,
                                        "branch_ar": "فرع صالح بن علي",
                                        "branch_en": "Saleh bin Ali Branch",
                                        "notes": "",
                                        "children": [
                                            {
                                                "id": "abdelqader_saleh",
                                                "name_ar": "عبد القادر",
                                                "name_en": "Abdel Qader",
                                                "generation": 5,
                                                "children": [
                                                    {
                                                        "id": "saleh_abdelqader",
                                                        "name_ar": "صالح",
                                                        "name_en": "Saleh",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "mohanad_saleh_aq",
                                                                "name_ar": "مهند",
                                                                "name_en": "Mohanad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "saleh_mohanad_aq", "name_ar": "صالح", "name_en": "Saleh", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "mohd_saleh_aq",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "obaida_mohd_aq", "name_ar": "عبيدة", "name_en": "Obaida", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "id": "subhi_abdelqader",
                                                        "name_ar": "صبحي",
                                                        "name_en": "Subhi",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "sabri_subhi",
                                                                "name_ar": "صبري",
                                                                "name_en": "Sabri",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "raed_sabri", "name_ar": "رائد", "name_en": "Raed", "generation": 8, "children": []},
                                                                    {"id": "abdelqader_sabri", "name_ar": "عبد القادر", "name_en": "Abdel Qader", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "mahmoud_subhi",
                                                                "name_ar": "محمود",
                                                                "name_en": "Mahmoud",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "tariq_mahmoud_s", "name_ar": "طارق", "name_en": "Tariq", "generation": 8, "children": []},
                                                                    {"id": "mohd_mahmoud_s", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "amr_mahmoud_s", "name_ar": "عمرو", "name_en": "Amr", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "mohd_subhi",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "baraa_mohd_subhi", "name_ar": "براء", "name_en": "Baraa", "generation": 8, "children": []},
                                                                    {"id": "rayan_mohd_subhi", "name_ar": "ريان", "name_en": "Rayan", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "mohd_saleh",
                                                "name_ar": "محمد",
                                                "name_en": "Muhammad",
                                                "generation": 5,
                                                "children": [
                                                    {"id": "fouad_mohd_s", "name_ar": "فؤاد", "name_en": "Fouad", "generation": 6, "children": []},
                                                    {
                                                        "id": "ghassan_mohd_s",
                                                        "name_ar": "غسان",
                                                        "name_en": "Ghassan",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "bakr_ghassan_s", "name_ar": "بكر", "name_en": "Bakr", "generation": 7, "children": []},
                                                            {"id": "omar_ghassan_s", "name_ar": "عمر", "name_en": "Omar", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "fareed_mohd_s",
                                                        "name_ar": "فريد",
                                                        "name_en": "Fareed",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "mohd_fareed_s",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "fareed_mohd_fs", "name_ar": "فريد", "name_en": "Fareed", "generation": 8, "children": []},
                                                                    {"id": "ibrahim_mohd_fs", "name_ar": "ابراهيم", "name_en": "Ibrahim", "generation": 8, "children": []},
                                                                    {"id": "ahmad_mohd_fs", "name_ar": "احمد", "name_en": "Ahmad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "maher_fareed_s", "name_ar": "ماهر", "name_en": "Maher", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "mustafa_mohd_s",
                                                        "name_ar": "مصطفي",
                                                        "name_en": "Mustafa",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "ahmad_mustafa_ms",
                                                                "name_ar": "احمد",
                                                                "name_en": "Ahmad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "mustafa_ahmad_mms", "name_ar": "مصطفي", "name_en": "Mustafa", "generation": 8, "children": []},
                                                                    {"id": "abdelrahman_ahmad_mms", "name_ar": "عبد الرحمن", "name_en": "Abdel Rahman", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "mohd_mustafa_ms",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "elias_mohd_mms", "name_ar": "الياس", "name_en": "Elias", "generation": 8, "children": []},
                                                                    {"id": "arkan_mohd_mms", "name_ar": "اركان", "name_en": "Arkan", "generation": 8, "children": []},
                                                                    {"id": "rayan_mohd_mms", "name_ar": "ريان", "name_en": "Rayan", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "saleh_mustafa_ms",
                                                                "name_ar": "صالح",
                                                                "name_en": "Saleh",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "omar_saleh_mms", "name_ar": "عمر", "name_en": "Omar", "generation": 8, "children": []},
                                                                    {"id": "karam_saleh_mms", "name_ar": "كرم", "name_en": "Karam", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "islam_mustafa_ms",
                                                                "name_ar": "اسلام",
                                                                "name_en": "Islam",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "layth_islam_mms", "name_ar": "ليث", "name_en": "Layth", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "ehab_mustafa_ms",
                                                                "name_ar": "ايهاب",
                                                                "name_en": "Ihab",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "qais_ehab_mms", "name_ar": "قيس", "name_en": "Qais", "generation": 8, "children": []},
                                                                    {"id": "adam_ehab_mms", "name_ar": "ادم", "name_en": "Adam", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "id": "khaled_mohd_s",
                                                        "name_ar": "خالد",
                                                        "name_en": "Khaled",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "walid_khaled_s", "name_ar": "وليد", "name_en": "Walid", "generation": 7, "children": []},
                                                            {"id": "mohd_khaled_s", "name_ar": "محمد", "name_en": "Muhammad", "generation": 7, "children": []},
                                                            {"id": "karam_khaled_s", "name_ar": "كرم", "name_en": "Karam", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "fadl_mohd_s",
                                                        "name_ar": "فضل",
                                                        "name_en": "Fadl",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "mohd_fadl_s", "name_ar": "محمد", "name_en": "Muhammad", "generation": 7, "children": []},
                                                            {"id": "ibrahim_fadl_s", "name_ar": "ابراهيم", "name_en": "Ibrahim", "generation": 7, "children": []}
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    # 2.2 نمر بن علي
                                    {
                                        "id": "nimr_ali",
                                        "name_ar": "نمر",
                                        "name_en": "Nimr",
                                        "generation": 4,
                                        "branch_ar": "فرع نمر بن علي",
                                        "branch_en": "Nimr bin Ali Branch",
                                        "notes": "",
                                        "children": [
                                            {
                                                "id": "ali_nimr",
                                                "name_ar": "علي",
                                                "name_en": "Ali",
                                                "generation": 5,
                                                "children": [
                                                    {
                                                        "id": "omar_ali_nimr",
                                                        "name_ar": "عمر",
                                                        "name_en": "Omar",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "ghazi_omar_n",
                                                                "name_ar": "غازي",
                                                                "name_en": "Ghazi",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "nidal_ghazi", "name_ar": "نضال", "name_en": "Nidal", "generation": 8, "children": []},
                                                                    {"id": "ayman_ghazi", "name_ar": "ايمن", "name_en": "Ayman", "generation": 8, "children": []},
                                                                    {"id": "mohd_ghazi", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "jehad_ghazi", "name_ar": "جهاد", "name_en": "Jehad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "nawwaf_omar_n",
                                                                "name_ar": "نواف",
                                                                "name_en": "Nawwaf",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "omar_nawwaf_on",
                                                                        "name_ar": "عمر",
                                                                        "name_en": "Omar",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "omar_omar_non", "name_ar": "عمر", "name_en": "Omar", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {
                                                                        "id": "ali_nawwaf_on",
                                                                        "name_ar": "علي",
                                                                        "name_en": "Ali",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "ahmad_ali_non", "name_ar": "احمد", "name_en": "Ahmad", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {
                                                                        "id": "mohd_nawwaf_on",
                                                                        "name_ar": "محمد",
                                                                        "name_en": "Muhammad",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "mahmoud_mohd_non", "name_ar": "محمود", "name_en": "Mahmoud", "generation": 9, "children": []},
                                                                            {"id": "rabee_mohd_non", "name_ar": "ربيع", "name_en": "Rabee", "generation": 9, "children": []},
                                                                            {"id": "nawwaf_mohd_non", "name_ar": "نواف", "name_en": "Nawwaf", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {
                                                                        "id": "mazen_nawwaf_on",
                                                                        "name_ar": "مازن",
                                                                        "name_en": "Mazen",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "malik_mazen_non", "name_ar": "مالك", "name_en": "Malik", "generation": 9, "children": []},
                                                                            {"id": "abdelrahman_mazen_non", "name_ar": "عبد الرحمن", "name_en": "Abdel Rahman", "generation": 9, "children": []}
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "id": "abdullah_omar_n",
                                                                "name_ar": "عبد اللة",
                                                                "name_en": "Abdullah",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "nawwaf_abdullah_on", "name_ar": "نواف", "name_en": "Nawwaf", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "mohd_omar_n",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "bassam_mohd_on", "name_ar": "بسام", "name_en": "Bassam", "generation": 8, "children": []},
                                                                    {"id": "samer_mohd_on", "name_ar": "سامر", "name_en": "Samer", "generation": 8, "children": []},
                                                                    {"id": "mowafaq_mohd_on", "name_ar": "موفق", "name_en": "Mowafaq", "generation": 8, "children": []},
                                                                    {
                                                                        "id": "ahmad_mohd_on",
                                                                        "name_ar": "احمد",
                                                                        "name_en": "Ahmad",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "khaled_ahmad_mon", "name_ar": "خالد", "name_en": "Khaled", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {
                                                                        "id": "majed_mohd_on",
                                                                        "name_ar": "ماجد",
                                                                        "name_en": "Majed",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "rayan_majed_mon", "name_ar": "ريان", "name_en": "Rayan", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {
                                                                        "id": "zakaria_mohd_on",
                                                                        "name_ar": "زكريا",
                                                                        "name_en": "Zakaria",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "yahya_zakaria_mon", "name_ar": "يحيي", "name_en": "Yahya", "generation": 9, "children": []}
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "id": "ali_omar_n",
                                                                "name_ar": "علي",
                                                                "name_en": "Ali",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "marwan_ali_on",
                                                                        "name_ar": "مروان",
                                                                        "name_en": "Marwan",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "ahmad_marwan", "name_ar": "احمد", "name_en": "Ahmad", "generation": 9, "children": []},
                                                                            {"id": "ali_marwan", "name_ar": "علي", "name_en": "Ali", "generation": 9, "children": []}
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            {
                                                "id": "ahmad_nimr",
                                                "name_ar": "احمد",
                                                "name_en": "Ahmad",
                                                "generation": 5,
                                                "children": [
                                                    {
                                                        "id": "mohd_fathi_ahmad_n",
                                                        "name_ar": "محمد فتحي",
                                                        "name_en": "Muhammad Fathi",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "ahmad_mf", "name_ar": "احمد", "name_en": "Ahmad", "generation": 7, "children": []},
                                                            {
                                                                "id": "jamal_mf",
                                                                "name_ar": "جمال",
                                                                "name_en": "Jamal",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "khaled_jamal_mf", "name_ar": "خالد", "name_en": "Khaled", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "ali_mf", "name_ar": "علي", "name_en": "Ali", "generation": 7, "children": []},
                                                            {
                                                                "id": "nimr_mf",
                                                                "name_ar": "نمر",
                                                                "name_en": "Nimr",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "islam_nimr_mf", "name_ar": "اسلام", "name_en": "Islam", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "hussam_mf",
                                                                "name_ar": "حسام",
                                                                "name_en": "Hussam",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "morad_hussam_mf", "name_ar": "مراد", "name_en": "Morad", "generation": 8, "children": []},
                                                                    {"id": "ahmad_hussam_mf", "name_ar": "احمد", "name_en": "Ahmad", "generation": 8, "children": []},
                                                                    {"id": "mohd_hussam_mf", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    # 2.3 محمد بن علي
                                    {
                                        "id": "mohd_ali_h",
                                        "name_ar": "محمد",
                                        "name_en": "Muhammad",
                                        "generation": 4,
                                        "branch_ar": "فرع محمد بن علي",
                                        "branch_en": "Muhammad bin Ali Branch",
                                        "notes": "",
                                        "children": [
                                            {
                                                "id": "ibrahim_mohd_ali",
                                                "name_ar": "ابراهيم",
                                                "name_en": "Ibrahim",
                                                "generation": 5,
                                                "children": [
                                                    {
                                                        "id": "nizam_ibrahim",
                                                        "name_ar": "نظام",
                                                        "name_en": "Nizam",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "ibrahim_nizam",
                                                                "name_ar": "ابراهيم",
                                                                "name_en": "Ibrahim",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "nizam_ibrahim_n", "name_ar": "نظام", "name_en": "Nizam", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "mohanad_nizam", "name_ar": "مهند", "name_en": "Mohanad", "generation": 7, "children": []},
                                                            {"id": "ehab_nizam", "name_ar": "ايهاب", "name_en": "Ihab", "generation": 7, "children": []},
                                                            {"id": "emad_nizam", "name_ar": "عماد", "name_en": "Emad", "generation": 7, "children": []},
                                                            {"id": "rami_nizam", "name_ar": "رامي", "name_en": "Rami", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {"id": "zahran_ibrahim", "name_ar": "زهران", "name_en": "Zahran", "generation": 6, "children": []},
                                                    {
                                                        "id": "mazhar_ibrahim",
                                                        "name_ar": "مزهر",
                                                        "name_en": "Mazhar",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "mohd_mazhar", "name_ar": "محمد", "name_en": "Muhammad", "generation": 7, "children": []},
                                                            {"id": "nadeem_mazhar", "name_ar": "نديم", "name_en": "Nadeem", "generation": 7, "children": []},
                                                            {"id": "raafat_mazhar", "name_ar": "رافت", "name_en": "Raafat", "generation": 7, "children": []},
                                                            {"id": "bandar_mazhar", "name_ar": "بندر", "name_en": "Bandar", "generation": 7, "children": []},
                                                            {"id": "khaled_mazhar", "name_ar": "خالد", "name_en": "Khaled", "generation": 7, "children": []},
                                                            {"id": "motasem_mazhar", "name_ar": "معتصم", "name_en": "Moatasem", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "sharif_ibrahim",
                                                        "name_ar": "شريف",
                                                        "name_en": "Sharif",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "hisham_sharif",
                                                                "name_ar": "هشام",
                                                                "name_en": "Hisham",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "sharif_hisham", "name_ar": "شريف", "name_en": "Sharif", "generation": 8, "children": []},
                                                                    {"id": "mustafa_hisham", "name_ar": "مصطفي", "name_en": "Mustafa", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    # 2.4 حسين بن علي
                                    {
                                        "id": "hussein_ali_h",
                                        "name_ar": "حسين",
                                        "name_en": "Hussein",
                                        "generation": 4,
                                        "branch_ar": "فرع حسين بن علي",
                                        "branch_en": "Hussein bin Ali Branch",
                                        "notes": "",
                                        "children": [
                                            {
                                                "id": "jaber_hussein",
                                                "name_ar": "جابر",
                                                "name_en": "Jaber",
                                                "generation": 5,
                                                "children": [
                                                    {
                                                        "id": "azmi_jaber",
                                                        "name_ar": "عزمي",
                                                        "name_en": "Azmi",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "mohd_azmi", "name_ar": "محمد", "name_en": "Muhammad", "generation": 7, "children": []},
                                                            {"id": "ahmad_azmi", "name_ar": "احمد", "name_en": "Ahmad", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {"id": "jameel_jaber", "name_ar": "جميل", "name_en": "Jamil", "generation": 6, "children": []},
                                                    {
                                                        "id": "jawdat_jaber",
                                                        "name_ar": "جودت",
                                                        "name_en": "Jawdat",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "jaber_jawdat", "name_ar": "جابر", "name_en": "Jaber", "generation": 7, "children": []},
                                                            {
                                                                "id": "mohd_jawdat",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "ibrahim_mohd_j",
                                                                        "name_ar": "ابراهيم",
                                                                        "name_en": "Ibrahim",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "mohd_ibrahim_mj", "name_ar": "محمد", "name_en": "Muhammad", "generation": 9, "children": []},
                                                                            {"id": "yahya_ibrahim_mj", "name_ar": "يحيي", "name_en": "Yahya", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {"id": "aws_mohd_j", "name_ar": "اوس", "name_en": "Aws", "generation": 8, "children": []},
                                                                    {"id": "elias_mohd_j", "name_ar": "الياس", "name_en": "Elias", "generation": 8, "children": []},
                                                                    {"id": "adam_mohd_j", "name_ar": "ادم", "name_en": "Adam", "generation": 8, "children": []},
                                                                    {"id": "nawras_mohd_j", "name_ar": "نورس", "name_en": "Nawras", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "ahmad_jawdat",
                                                                "name_ar": "احمد",
                                                                "name_en": "Ahmad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "omar_ahmad_j", "name_ar": "عمر", "name_en": "Omar", "generation": 8, "children": []},
                                                                    {"id": "jawdat_ahmad_j", "name_ar": "جودت", "name_en": "Jawdat", "generation": 8, "children": []},
                                                                    {"id": "mohd_ahmad_j", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "jameel_jawdat", "name_ar": "جميل", "name_en": "Jamil", "generation": 7, "children": []},
                                                            {
                                                                "id": "bassem_jawdat",
                                                                "name_ar": "باسم",
                                                                "name_en": "Bassem",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "akram_bassem", "name_ar": "اكرم", "name_en": "Akram", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    # 2.5 مسلم بن علي
                                    {
                                        "id": "muslim_ali",
                                        "name_ar": "مسلم",
                                        "name_en": "Muslim",
                                        "generation": 4,
                                        "branch_ar": "فرع مسلم بن علي",
                                        "branch_en": "Muslim bin Ali Branch",
                                        "notes": "",
                                        "children": [
                                            # 2.5.1 زكي بن مسلم
                                            {
                                                "id": "zaki_muslim",
                                                "name_ar": "زكي",
                                                "name_en": "Zaki",
                                                "generation": 5,
                                                "branch_ar": "فرع زكي بن مسلم",
                                                "branch_en": "Zaki bin Muslim Branch",
                                                "children": [
                                                    {
                                                        "id": "faisal_zaki",
                                                        "name_ar": "فيصل",
                                                        "name_en": "Faisal",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "nidal_faisal",
                                                                "name_ar": "نضال",
                                                                "name_en": "Nidal",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "faisal_nidal_z", "name_ar": "فيصل", "name_en": "Faisal", "generation": 8, "children": []},
                                                                    {"id": "ahmad_nidal_z", "name_ar": "احمد", "name_en": "Ahmad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "nasser_faisal", "name_ar": "ناصر", "name_en": "Nasser", "generation": 7, "children": []},
                                                            {
                                                                "id": "kamal_faisal",
                                                                "name_ar": "كمال",
                                                                "name_en": "Kamal",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "mohd_kamal_z", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "bashar_faisal",
                                                                "name_ar": "بشار",
                                                                "name_en": "Bashar",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "faisal_bashar_z", "name_ar": "فيصل", "name_en": "Faisal", "generation": 8, "children": []},
                                                                    {"id": "adnan_bashar_z", "name_ar": "عدنان", "name_en": "Adnan", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "id": "khalil_zaki",
                                                        "name_ar": "خليل",
                                                        "name_en": "Khalil",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "bahaa_khalil",
                                                                "name_ar": "بهاء",
                                                                "name_en": "Bahaa",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "khalil_bahaa", "name_ar": "خليل", "name_en": "Khalil", "generation": 8, "children": []},
                                                                    {"id": "ameer_bahaa", "name_ar": "امير", "name_en": "Ameer", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "moataz_khalil", "name_ar": "معتز", "name_en": "Moataz", "generation": 7, "children": []},
                                                            {
                                                                "id": "mohd_khalil",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "ali_mohd_kz", "name_ar": "علي", "name_en": "Ali", "generation": 8, "children": []},
                                                                    {"id": "yaqoub_mohd_kz", "name_ar": "يعقوب", "name_en": "Yaqoub", "generation": 8, "children": []},
                                                                    {"id": "omar_mohd_kz", "name_ar": "عمر", "name_en": "Omar", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "muath_khalil", "name_ar": "معاذ", "name_en": "Muath", "generation": 7, "children": []},
                                                            {"id": "hamza_khalil", "name_ar": "حمزة", "name_en": "Hamza", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "muslim_zaki",
                                                        "name_ar": "مسلم",
                                                        "name_en": "Muslim",
                                                        "generation": 6,
                                                        "notes": "وفاة 19/2/2016 الجمعة (Died Friday 19/02/2016)",
                                                        "children": [
                                                            {"id": "samer_muslim_z", "name_ar": "سامر", "name_en": "Samer", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "fahmi_zaki",
                                                        "name_ar": "فهمي",
                                                        "name_en": "Fahmi",
                                                        "generation": 6,
                                                        "notes": "وفاة 5/1/1982 (Died 05/01/1982)",
                                                        "children": [
                                                            {
                                                                "id": "zaki_fahmi",
                                                                "name_ar": "زكي",
                                                                "name_en": "Zaki",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "khaled_zaki_fz", "name_ar": "خالد", "name_en": "Khaled", "generation": 8, "children": []},
                                                                    {"id": "hussam_zaki_fz", "name_ar": "حسام", "name_en": "Hussam", "generation": 8, "children": []},
                                                                    {"id": "mohd_zaki_fz", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "ahmad_zaki_fz", "name_ar": "احمد", "name_en": "Ahmad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "samir_fahmi", "name_ar": "سمير", "name_en": "Samir", "generation": 7, "children": []},
                                                            {
                                                                "id": "muneer_fahmi",
                                                                "name_ar": "منير",
                                                                "name_en": "Muneer",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "wisam_muneer", "name_ar": "وسام", "name_en": "Wissam", "generation": 8, "children": []},
                                                                    {"id": "wiam_muneer", "name_ar": "وئام", "name_en": "Wiam", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "emad_fahmi",
                                                                "name_ar": "عماد",
                                                                "name_en": "Emad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "naseem_emad", "name_ar": "نسيم", "name_en": "Naseem", "generation": 8, "children": []},
                                                                    {"id": "nadeem_emad", "name_ar": "نديم", "name_en": "Nadeem", "generation": 8, "children": []},
                                                                    {"id": "hamza_emad", "name_ar": "حمزة", "name_en": "Hamza", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            # 2.5.2 شاكر بن مسلم
                                            {
                                                "id": "shaker_muslim",
                                                "name_ar": "شاكر",
                                                "name_en": "Shaker",
                                                "generation": 5,
                                                "branch_ar": "فرع شاكر بن مسلم",
                                                "branch_en": "Shaker bin Muslim Branch",
                                                "children": [
                                                    {
                                                        "id": "abdelrahim_shaker",
                                                        "name_ar": "عبد الرحيم",
                                                        "name_en": "Abdel Rahim",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "najwan_ar", "name_ar": "نجوان", "name_en": "Najwan", "generation": 7, "children": []},
                                                            {
                                                                "id": "raslan_ar",
                                                                "name_ar": "رسلان",
                                                                "name_en": "Raslan",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "mohd_raslan",
                                                                        "name_ar": "محمد",
                                                                        "name_en": "Muhammad",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "raslan_mohd_r", "name_ar": "رسلان", "name_en": "Raslan", "generation": 9, "children": []},
                                                                            {"id": "rayan_mohd_r", "name_ar": "ريان", "name_en": "Rayan", "generation": 9, "children": []},
                                                                            {"id": "yaman_mohd_r", "name_ar": "يمان", "name_en": "Yaman", "generation": 9, "children": []},
                                                                            {
                                                                                "id": "abdelrahman_mohd_r",
                                                                                "name_ar": "عبد الرحمن",
                                                                                "name_en": "Abdel Rahman",
                                                                                "generation": 9,
                                                                                "children": [
                                                                                    {"id": "ameer_abdelrahman_mr", "name_ar": "امير", "name_en": "Ameer", "generation": 10, "children": []}
                                                                                ]
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {"id": "ghassan_ar", "name_ar": "غسان", "name_en": "Ghassan", "generation": 7, "children": []},
                                                            {"id": "bassam_ar", "name_ar": "بسام", "name_en": "Bassam", "generation": 7, "children": []},
                                                            {"id": "rashdan_ar", "name_ar": "رشدان", "name_en": "Rashdan", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "hussein_shaker",
                                                        "name_ar": "حسين",
                                                        "name_en": "Hussein",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "shaker_hussein_s",
                                                                "name_ar": "شاكر",
                                                                "name_en": "Shaker",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "raed_shaker_hs", "name_ar": "رائد", "name_en": "Raed", "generation": 8, "children": []},
                                                                    {
                                                                        "id": "saed_shaker_hs",
                                                                        "name_ar": "سائد",
                                                                        "name_en": "Saed",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "shaker_saed", "name_ar": "شاكر", "name_en": "Shaker", "generation": 9, "children": []},
                                                                            {"id": "saed_saed", "name_ar": "سائد", "name_en": "Saed", "generation": 9, "children": []}
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "id": "majed_hussein_s",
                                                                "name_ar": "ماجد",
                                                                "name_en": "Majed",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "ehab_majed_hs",
                                                                        "name_ar": "ايهاب",
                                                                        "name_en": "Ihab",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "majed_ehab_mhs", "name_ar": "ماجد", "name_en": "Majed", "generation": 9, "notes": "رامي الحمد الله", "children": []},
                                                                            {"id": "ehab_ehab_mhs", "name_ar": "ايهاب", "name_en": "Ihab", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {"id": "alaa_majed_hs", "name_ar": "علاء", "name_en": "Alaa", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "sofian_hussein_s", "name_ar": "سفيان", "name_en": "Sofian", "generation": 7, "children": []},
                                                            {"id": "jehad_hussein_s", "name_ar": "جهاد", "name_en": "Jehad", "generation": 7, "children": []},
                                                            {
                                                                "id": "iyad_hussein_s",
                                                                "name_ar": "اياد",
                                                                "name_en": "Iyad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "mohd_iyad_hs",
                                                                        "name_ar": "محمد",
                                                                        "name_en": "Muhammad",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "enan_mohd_ihs", "name_ar": "عنان", "name_en": "Enan", "generation": 9, "children": []},
                                                                            {
                                                                                "id": "ammar_mohd_ihs",
                                                                                "name_ar": "عمار",
                                                                                "name_en": "Ammar",
                                                                                "generation": 9,
                                                                                "children": [
                                                                                    {"id": "karam_ammar_mihs", "name_ar": "كرم", "name_en": "Karam", "generation": 10, "children": []}
                                                                                ]
                                                                            },
                                                                            {"id": "amer_mohd_ihs", "name_ar": "عامر", "name_en": "Amer", "generation": 9, "children": []}
                                                                        ]
                                                                    }
                                                                ]
                                                            },
                                                            {
                                                                "id": "emad_hussein_s",
                                                                "name_ar": "عماد",
                                                                "name_en": "Emad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "hussein_emad_hs",
                                                                        "name_ar": "حسين",
                                                                        "name_en": "Hussein",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "emad_hussein_ehs", "name_ar": "عماد", "name_en": "Emad", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {"id": "mohd_emad_hs", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "jad_emad_hs", "name_ar": "جاد", "name_en": "Jad", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            # 2.5.3 شكري بن مسلم
                                            {
                                                "id": "shukri_muslim",
                                                "name_ar": "شكري",
                                                "name_en": "Shukri",
                                                "generation": 5,
                                                "branch_ar": "فرع شكري بن مسلم",
                                                "branch_en": "Shukri bin Muslim Branch",
                                                "children": [
                                                    {
                                                        "id": "hassan_shukri",
                                                        "name_ar": "حسان",
                                                        "name_en": "Hassan",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "tameem_hassan_s", "name_ar": "تميم", "name_en": "Tameem", "generation": 7, "children": []},
                                                            {"id": "duraid_hassan_s", "name_ar": "دريد", "name_en": "Duraid", "generation": 7, "children": []},
                                                            {"id": "suhaib_hassan_s", "name_ar": "صهيب", "name_en": "Suhaib", "generation": 7, "children": []},
                                                            {
                                                                "id": "rami_hassan_s",
                                                                "name_ar": "رامي",
                                                                "name_en": "Rami",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "ihsan_rami_hs", "name_ar": "احسان", "name_en": "Ihsan", "generation": 8, "children": []},
                                                                    {"id": "abdullah_rami_hs", "name_ar": "عبدالله", "name_en": "Abdullah", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "qusay_hassan_s", "name_ar": "قصي", "name_en": "Qusay", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "waheb_shukri",
                                                        "name_ar": "وهيب",
                                                        "name_en": "Waheb",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "fares_waheb", "name_ar": "فارس", "name_en": "Fares", "generation": 7, "children": []},
                                                            {"id": "salah_aldeen_waheb", "name_ar": "صلاح الدين", "name_en": "Salah Al-Deen", "generation": 7, "children": []},
                                                            {"id": "hassan_waheb", "name_ar": "حسان", "name_en": "Hassan", "generation": 7, "children": []},
                                                            {"id": "bilal_waheb", "name_ar": "بلال", "name_en": "Bilal", "generation": 7, "children": []},
                                                            {
                                                                "id": "ashraf_waheb",
                                                                "name_ar": "اشرف",
                                                                "name_en": "Ashraf",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "abdelrahman_ashraf_w",
                                                                        "name_ar": "عبد الرحمن",
                                                                        "name_en": "Abdel Rahman",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "yaman_abdelrahman_aw", "name_ar": "يمان", "name_en": "Yaman", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {"id": "ahmad_ashraf_w", "name_ar": "احمد", "name_en": "Ahmad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "ayman_waheb",
                                                                "name_ar": "ايمن",
                                                                "name_en": "Ayman",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "ramez_ayman_w", "name_ar": "رامز", "name_en": "Ramez", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "anwar_waheb",
                                                                "name_ar": "انور",
                                                                "name_en": "Anwar",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "yazan_anwar_w", "name_ar": "يزن", "name_en": "Yazan", "generation": 8, "children": []},
                                                                    {"id": "karam_anwar_w", "name_ar": "كرم", "name_en": "Karam", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "ahmad_waheb",
                                                                "name_ar": "احمد",
                                                                "name_en": "Ahmad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "waheb_ahmad_w", "name_ar": "وهيب", "name_en": "Waheb", "generation": 8, "children": []},
                                                                    {"id": "mohd_ahmad_w", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "albaraa_ahmad_w", "name_ar": "البراء", "name_en": "Al-Baraa", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "afdal_waheb",
                                                                "name_ar": "افضل",
                                                                "name_en": "Afdal",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "kinan_afdal_w", "name_ar": "كنان", "name_en": "Kinan", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "akram_waheb",
                                                                "name_ar": "اكرم",
                                                                "name_en": "Akram",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "mohd_akram_w", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "id": "haseeb_shukri",
                                                        "name_ar": "حسيب",
                                                        "name_en": "Haseeb",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "shukri_haseeb",
                                                                "name_ar": "شكري",
                                                                "name_en": "Shukri",
                                                                "generation": 7,
                                                                "children": [
                                                                    {
                                                                        "id": "ehab_shukri_h",
                                                                        "name_ar": "ايهاب",
                                                                        "name_en": "Ihab",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "tameem_ehab_sh", "name_ar": "تميم", "name_en": "Tameem", "generation": 9, "children": []},
                                                                            {"id": "aws_ehab_sh", "name_ar": "اوس", "name_en": "Aws", "generation": 9, "children": []}
                                                                        ]
                                                                    },
                                                                    {"id": "haseeb_shukri_h", "name_ar": "حسيب", "name_en": "Haseeb", "generation": 8, "children": []},
                                                                    {"id": "mohd_shukri_h", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {
                                                                        "id": "nouraldeen_shukri_h",
                                                                        "name_ar": "نور الدين",
                                                                        "name_en": "Nour Al-Deen",
                                                                        "generation": 8,
                                                                        "children": [
                                                                            {"id": "shukri_nouraldeen_sh", "name_ar": "شكري", "name_en": "Shukri", "generation": 9, "children": []}
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                                ]
                                            },
                                            # 2.5.4 ناجي بن مسلم
                                            {
                                                "id": "naji_muslim",
                                                "name_ar": "ناجي",
                                                "name_en": "Naji",
                                                "generation": 5,
                                                "branch_ar": "فرع ناجي بن مسلم",
                                                "branch_en": "Naji bin Muslim Branch",
                                                "children": [
                                                    {
                                                        "id": "najati_naji",
                                                        "name_ar": "نجاتي",
                                                        "name_en": "Najati",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "naji_najati",
                                                                "name_ar": "ناجي",
                                                                "name_en": "Naji",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "nasser_naji_nn", "name_ar": "ناصر", "name_en": "Nasser", "generation": 8, "children": []},
                                                                    {"id": "mohd_naji_nn", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "abdelrahman_naji_nn", "name_ar": "عبد الرحمن", "name_en": "Abdel Rahman", "generation": 8, "children": []},
                                                                    {"id": "adam_naji_nn", "name_ar": "ادم", "name_en": "Adam", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "nashat_najati",
                                                                "name_ar": "نشات",
                                                                "name_en": "Nashat",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "rayan_nashat_nn", "name_ar": "ريان", "name_en": "Rayan", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "nael_najati", "name_ar": "نائل", "name_en": "Nael", "generation": 7, "children": []},
                                                            {"id": "wael_najati", "name_ar": "وائل", "name_en": "Wael", "generation": 7, "children": []},
                                                            {
                                                                "id": "mohd_najati",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "abdullah_mohd_nj", "name_ar": "عبدالله", "name_en": "Abdullah", "generation": 8, "children": []},
                                                                    {"id": "fares_mohd_nj", "name_ar": "فارس", "name_en": "Fares", "generation": 8, "children": []},
                                                                    {"id": "hussein_mohd_nj", "name_ar": "حسين", "name_en": "Hussein", "generation": 8, "children": []}
                                                                ]
                                                            }
                                                        ]
                                                    },
                                                    {
                                                        "id": "mohd_naji_m",
                                                        "name_ar": "محمد",
                                                        "name_en": "Muhammad",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "majdi_mohd_nm",
                                                                "name_ar": "مجدي",
                                                                "name_en": "Majdi",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "ahmad_majdi_mnm", "name_ar": "احمد", "name_en": "Ahmad", "generation": 8, "children": []},
                                                                    {"id": "mohd_majdi_mnm", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "omar_majdi_mnm", "name_ar": "عمر", "name_en": "Omar", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "osama_mohd_nm",
                                                                "name_ar": "اسامة",
                                                                "name_en": "Osama",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "baraa_osama_mnm", "name_ar": "براء", "name_en": "Baraa", "generation": 8, "children": []},
                                                                    {"id": "youssef_osama_mnm", "name_ar": "يوسف", "name_en": "Youssef", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {
                                                                "id": "ahmad_mohd_nm",
                                                                "name_ar": "احمد",
                                                                "name_en": "Ahmad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "mohd_ahmad_mnm", "name_ar": "محمد", "name_en": "Muhammad", "generation": 8, "children": []},
                                                                    {"id": "yahya_ahmad_mnm", "name_ar": "يحيي", "name_en": "Yahya", "generation": 8, "children": []},
                                                                    {"id": "malik_ahmad_mnm", "name_ar": "مالك", "name_en": "Malik", "generation": 8, "children": []},
                                                                    {"id": "ibrahim_ahmad_mnm", "name_ar": "ابراهيم", "name_en": "Ibrahim", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "anas_mohd_nm", "name_ar": "انس", "name_en": "Anas", "generation": 7, "children": []},
                                                            {"id": "abdullah_mohd_nm", "name_ar": "عبدالله", "name_en": "Abdullah", "generation": 7, "children": []}
                                                        ]
                                                    }
                                                ]
                                            },
                                            # 2.5.5 محمد بن مسلم
                                            {
                                                "id": "mohd_muslim",
                                                "name_ar": "محمد",
                                                "name_en": "Muhammad",
                                                "generation": 5,
                                                "branch_ar": "فرع محمد بن مسلم",
                                                "branch_en": "Muhammad bin Muslim Branch",
                                                "children": [
                                                    {
                                                        "id": "riad_mohd_mus",
                                                        "name_ar": "رياض",
                                                        "name_en": "Riad",
                                                        "generation": 6,
                                                        "children": [
                                                            {
                                                                "id": "mohd_riad_mus",
                                                                "name_ar": "محمد",
                                                                "name_en": "Muhammad",
                                                                "generation": 7,
                                                                "children": [
                                                                    {"id": "riad_mohd_rm", "name_ar": "رياض", "name_en": "Riad", "generation": 8, "children": []}
                                                                ]
                                                            },
                                                            {"id": "walid_riad_mus", "name_ar": "وليد", "name_en": "Walid", "generation": 7, "children": []},
                                                            {"id": "maan_riad_mus", "name_ar": "معن", "name_en": "Maan", "generation": 7, "children": []},
                                                            {"id": "khaled_riad_mus", "name_ar": "خالد", "name_en": "Khaled", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "yahya_mohd_mus",
                                                        "name_ar": "يحيي",
                                                        "name_en": "Yahya",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "mohd_yahya_mus", "name_ar": "محمد", "name_en": "Muhammad", "generation": 7, "children": []},
                                                            {"id": "ahmad_yahya_mus", "name_ar": "احمد", "name_en": "Ahmad", "generation": 7, "children": []},
                                                            {"id": "abdelnasser_yahya_mus", "name_ar": "عبد الناصر", "name_en": "Abdel Nasser", "generation": 7, "children": []},
                                                            {"id": "zakaria_yahya_mus", "name_ar": "زكريا", "name_en": "Zakaria", "generation": 7, "children": []},
                                                            {"id": "jehad_yahya_mus", "name_ar": "جهاد", "name_en": "Jehad", "generation": 7, "children": []},
                                                            {"id": "youssef_yahya_mus", "name_ar": "يوسف", "name_en": "Youssef", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "mohd_awad_mohd_mus",
                                                        "name_ar": "محمد عوض",
                                                        "name_en": "Muhammad Awad",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "riad_mohd_awad", "name_ar": "رياض", "name_en": "Riad", "generation": 7, "children": []},
                                                            {"id": "ishaq_mohd_awad", "name_ar": "اسحاق", "name_en": "Ishaq", "generation": 7, "children": []}
                                                        ]
                                                    },
                                                    {
                                                        "id": "ishaq_mohd_mus",
                                                        "name_ar": "اسحاق",
                                                        "name_en": "Ishaq",
                                                        "generation": 6,
                                                        "children": [
                                                            {"id": "hani_ishaq_mus", "name_ar": "هاني", "name_en": "Hani", "generation": 7, "children": []}
                                                        ]
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }

def main():
    tree = get_complete_tree()
    
    # Flatten and add father references, branch tags, full paths
    flat_list = []
    
    def process_node(node, parent=None, branch_ar="الأصل", branch_en="Root"):
        if node.get("branch_ar"):
            branch_ar = node["branch_ar"]
        if node.get("branch_en"):
            branch_en = node["branch_en"]
        
        node["parent_id"] = parent["id"] if parent else None
        node["parent_name_ar"] = parent["name_ar"] if parent else None
        node["parent_name_en"] = parent["name_en"] if parent else None
        node["branch_ar"] = branch_ar
        node["branch_en"] = branch_en
        
        # Calculate full lineage
        if parent and parent.get("lineage_ar"):
            node["lineage_ar"] = f"{node['name_ar']} بن {parent['lineage_ar']}"
            node["lineage_en"] = f"{node['name_en']} bin {parent['lineage_en']}"
        elif parent:
            node["lineage_ar"] = f"{node['name_ar']} بن {parent['name_ar']}"
            node["lineage_en"] = f"{node['name_en']} bin {parent['name_en']}"
        else:
            node["lineage_ar"] = node["name_ar"]
            node["lineage_en"] = node["name_en"]
            
        flat_list.append({
            "id": node["id"],
            "name_ar": node["name_ar"],
            "name_en": node["name_en"],
            "parent_id": node["parent_id"],
            "parent_name_ar": node["parent_name_ar"],
            "parent_name_en": node["parent_name_en"],
            "generation": node["generation"],
            "branch_ar": node["branch_ar"],
            "branch_en": node["branch_en"],
            "lineage_ar": node["lineage_ar"],
            "lineage_en": node["lineage_en"],
            "notes": node.get("notes", ""),
            "children_count": len(node.get("children", []))
        })
        
        for c in node.get("children", []):
            process_node(c, node, branch_ar, branch_en)
            
    process_node(tree)
    
    out_dir = r"C:\Users\user\.gemini\antigravity\scratch\al_nada_family_tree"
    json_path = os.path.join(out_dir, "family_tree.json")
    flat_path = os.path.join(out_dir, "family_members_flat.json")
    
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(tree, f, ensure_ascii=False, indent=2)
        
    with open(flat_path, "w", encoding="utf-8") as f:
        json.dump(flat_list, f, ensure_ascii=False, indent=2)
        
    print(f"Total members: {len(flat_list)}")
    print(f"Max generation: {max(m['generation'] for m in flat_list)}")
    
    # Statistics
    branches = {}
    for m in flat_list:
        b = m["branch_ar"]
        branches[b] = branches.get(b, 0) + 1
    print("Branches distribution:", branches)

if __name__ == "__main__":
    main()
