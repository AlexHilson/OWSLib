# Example script that performs a set of (small) live requests versus the live CEDA WPS service

from owslib.wps import WebProcessingService, WPSExecution, WFSFeatureCollection, WFSQuery, GMLMultiPolygonFeatureCollection, monitorExecution, ComplexData, printInputOutput
from owslib.wps_utils import dump

verbose = True
wps = WebProcessingService('http://ceda-wps2.badc.rl.ac.uk/wps', verbose=verbose)

'''
# 1) GetCapabilities
# GET request: http://ceda-wps2.badc.rl.ac.uk/wps?Service=WPS&Request=GetCapabilities&Format=text/xml
wps.getcapabilities()

print 'WPS Identification type: %s' % wps.identification.type
print 'WPS Identification title: %s' % wps.identification.title
print 'WPS Identification abstract: %s' % wps.identification.abstract
for operation in wps.operations:
    print 'WPS Operation: %s' % operation.name
for process in wps.processes:
    print 'WPS Process: identifier=%s title=%s' % (process.identifier, process.title)
'''
    
# 2) DescribeProcess
# GET request: http://ceda-wps2.badc.rl.ac.uk/wps?identifier=DoubleIt&version=1.0.0&request=DescribeProcess&service=WPS

process = wps.describeprocess('DoubleIt')
print 'WPS Process: identifier=%s' % process.identifier
print 'WPS Process: title=%s' % process.title
print 'WPS Process: abstract=%s' % process.abstract
for input in process.dataInputs:
    print 'Process input:'
    printInputOutput(input, indent='\t')
for output in process.processOutputs:
    print 'Process output:'
    printInputOutput(output, indent='\t')

'''
for input in process.dataInputs:
    print 'Process input: identifier=%s, title=%s, abstract=%s, data type=%s, minOccurs=%d, maxOccurs=%d' % (input.identifier, input.title, input.abstract, input.dataType, input.minOccurs, input.maxOccurs)
    for value in input.allowedValues:
        print '\tAllowed Value: %s' % value
    for value in input.supportedValues:
        print '\tSupported Value: mimeType=%s, encoding=%s, schema=%s' % (value.mimeType, value.encoding, value.schema)
    print '\tDefault Value: %s ' % input.defaultValue
for output in process.processOutputs:
    print 'Process output: identifier=%s, title=%s, abstract=%s, data type=%s' % (output.identifier, output.title, output.abstract, output.dataType)
    for value in output.allowedValues:
        print '\tAllowed Value: %s' % value
    for value in output.supportedValues:
        if isinstance(value, ComplexData):
            print '\tSupported Value: mimeType=%s, encoding=%s, schema=%s' % (value.mimeType, value.encoding, value.schema)
        else:
            print '\tSupported Value: %s' % value
    print '\tDefault Value: %s ' % output.defaultValue
    for value in output.data:
        print '\tData Value: %s' % value
'''
