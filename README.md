# McAfee Config Decryptor

Tested up to version 10.7.0.667.17 of McAfee Endpoint Security.

## Usage
First, get the encrypted McAfee config file. Easiest way is to use the ESConfigTool (run as admin):

```shell
ESConfigTool.exe /export c:\temp\config.bin
```

Then, run the decryptor:

```shell
python decrypt.py config.bin

<ENSConfiguration toolVersion="2.0">
    <policies>
        <module name="Endpoint Security Platform">
            <businessObject id="AP" version="2.0">
                <General>
                    <Available>true</Available>
                    <Managed>false</Managed>
                    <EnabledInMC>true</EnabledInMC>
                    <NonCompliantFlags>0</NonCompliantFlags>
                    <FilterSecs>300</FilterSecs>
                    <FilterType>0</FilterType>
                    <AacCoreVersion>SYSCORE.19.7.0.195</AacCoreVersion>
                    <DefEventMapFile>C:\Program Files\McAfee\Endpoint Security\Endpoint Security Platform\EmDefXlateMap.xml</DefEventMapFile>
                </General>
                <Initiator>
                    <CsvInclude />
                    <CsvExclude />
                    <Executables></Executables>
                </Initiator>
                <Groups></Groups>
                <Rules></Rules>
                
                [..]

                </xs:schema>
            </businessObject>
        </module>
    </policyContracts>
</ENSConfiguration>
```