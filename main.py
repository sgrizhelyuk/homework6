def process_parsing_visit_log():
    visit_file = open('csvs/visit_log.csv', 'r')
    next(visit_file)
    with open('csvs/funnel.csv', 'w') as funnel_file:
        funnel_file.write('user_id,source,category\n')
        for line in visit_file:
            parts = line.split(',')
            user_id = parts[0]
            source = parts[1]
            if source.strip() != 'None' and source.strip() != 'other' and source.strip() != 'context':
                category = source
                category = category.strip()
                funnel_file.write(f'{user_id},{source.strip()},{category}\n')

if __name__ == "__main__":
    process_parsing_visit_log()