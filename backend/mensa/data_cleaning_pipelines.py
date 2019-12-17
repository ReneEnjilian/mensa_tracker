from mensa.time_calculator import calculate_days

class DataCleaningPipeline(object):
    def process_item(self, item, spider):
        
        if spider.name == "AllTU":
            space_cleaned_item = self.clean_spaces_all(item)
            price_adjusted_item = self.adjust_prices_all(space_cleaned_item)
            adjust_date_item = self.adjust_date_personalkantine_and_all(price_adjusted_item, spider)
            return adjust_date_item

        elif spider.name == "Mathecafe":
            
            price_adjusted_item = self.adjust_prices(item)
            cleaned_html_item = self.clean_corrupted_html(price_adjusted_item)
            adjusted_date_item = self.adjust_date_mathe_cafe(cleaned_html_item)
            #return adjusted_date_item
            return adjusted_date_item
            
        elif spider.name == "Personalkantine":
            price_adjusted_item = self.adjust_prices(item)
            cleaned_html_item = self.clean_corrupted_html(price_adjusted_item)
            adjusted_date_item = self.adjust_date_personalkantine_and_all(item, spider)
            # return adjusted_date_item
            return adjusted_date_item

        else:
            raise Exception("This spider doesnt exist!")


    def clean_spaces_all(self, item):
        for field in item:
            field_len = len(item[field])
            for i in range(field_len):
                new_field_item = item[field][i].strip()
                item[field][i] = new_field_item

        return item
    
    def adjust_prices_all(self, item):
        for field in item:
            if "price" in field:
                field_len = len(item[field])
                for i in range(field_len):
                    if item[field][i] is '':
                        item[field][i] = "free"
                    else:
                        data = item[field][i]
                        splitted = data.split()
                        prices = splitted[1]
                        student_price = prices.split("/")[0]
                        student_price = student_price.replace(",", ".")
                        item[field][i] = student_price
        return item

    def adjust_prices(self, item):
        
        for field in item:
            if "price" in field:
                price_list = []
                new_price = item[field][0].split("€")[0].strip()
                new_price = new_price.replace(",", ".")
                price_list.append(new_price)
                item[field] = price_list

        return item
    

    def clean_corrupted_html(self, item):
        for field in item:
            text_list = []
            new_text_data = item[field][0].replace(u'\xa0', u' ')
            text_list.append(new_text_data)
            item[field] = text_list
        return item
    
    def adjust_date_personalkantine_and_all(self, item, spider):
        
        prevoius_date = item["date"][0].split(",")[1].strip()
        date_as_list = []
        year = prevoius_date.split(".")[2]
        month = prevoius_date.split(".")[1]
        day = prevoius_date.split(".")[0]
        new_date = year + "-" + month + "-" + day
        date_as_list.append(new_date)
        item["date"] = date_as_list
        return item
    
    def adjust_date_mathe_cafe(self, item):
        dates = calculate_days()
        current_date = item["date"][0]
        date_as_list = []
        if current_date == 'Montag':
            date_as_list.append(dates[0])
            item["date"] = date_as_list
        elif current_date == 'Dienstag':
            date_as_list.append(dates[1])
            item["date"] = date_as_list
        elif current_date == 'Mittwoch':
            date_as_list.append(dates[2])
            item["date"] = date_as_list
        elif current_date == 'Donnerstag':
            date_as_list.append(dates[3])
            item["date"] = date_as_list
        elif current_date == 'Freitag':
            date_as_list.append(dates[4])
            item["date"] = date_as_list


        return item
    
        



