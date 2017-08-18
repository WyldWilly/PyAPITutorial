#<Component>
#   <Comment>135 - 146 MMOL/L</Comment>
#   <ComponentId>7</ComponentId>
#   <Flag/>
#   <High/>
#   <Low/>
#   <Name>Sodium(Na)</Name>
#   <ReferenceRange/>
#   <Unit/>
#   <Value>144</Value>
#</Component>
#<Component>
#   <Comment>145 - 146 MMOL/L</Comment>
#   <ComponentId>7</ComponentId>
#   <Flag/>
#   <High/>
#   <Low/>
#   <Name>Sodium(Na)</Name>
#   <ReferenceRange/>
#   <Unit/>
#   <Value>144</Value>
#</Component>

#data_from_server = http.get(...) XML

#python_data = parser(data_from_server)

components = [{
  'Comment': '145-146 MMOL/L',
  'ComponentId': 7
},{
'Comment': '145-186 MMOL/L',
  'ComponentId': 4
}]

for c in components:
    print(c['ComponentId'])

# in here, edit the mappings to be FHIR compliant

# output = jsonify(c)

