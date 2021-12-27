hhdvspkit::ISerialPortLibraryPtr library;
library.CreateInstance(__uuidof(hhdvspkit::SerialPortLibrary));
{
	auto port1 = library->createBridgePort(11);
	auto port2 = library->createBridgePort(10);
	port1->bridgePort = 10;
	port2->bridgePort = 11;
}
