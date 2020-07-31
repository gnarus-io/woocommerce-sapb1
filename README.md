# Woocommerce SAP B1

## Summary

This project is used to synchronize SAP Business One with Woocommerce.

The following entities are synchronized:

| SAP B1           | Direction | WooCommerce  | Description                                                             |
| ---------------- | --------- | ------------ | ----------------------------------------------------------------------- |
| Items            | -->       | Products     | Items in SAP are copied to Woocommerce (filtered by price list)         |
| Item Stock       | <--       | Stock        | Item stock levels in SAP are copied to Woocommerce                      |
| Business Partner | <--       | Customers    | Customers created in Woocommerce are copied to SAP as Business Partners |
| Sales Orders     | <--       | Orders       | Orders created in Woocommerce are copied to SAP as Sales Orders         |
| Deliveries       | -->       | Order Status | Deliveries in SAP will update order status in Woocommerce to Delivered  |

## Configuration

Configuration can be supplied in a .env file or as environment variables.

Available settings are:

| Setting      | Value                                                                                                                         |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| DIAPI        | SAP B1 DI COM object. You have to specify which version is installed in the SAP B1 server and will be loaded for the program. |
| SERVER       | SAP B1 Server name or IP address.                                                                                             |
| LANGUAGE     | Specify the default language for the company.                                                                                 |
| DBSERVERTYPE | Specify MS SQL server version.                                                                                                |
| COMPANYDB    | The company database name.                                                                                                    |
| B1USERNAME   | The SAP B1 user username for the connection.                                                                                  |
| B1PASSWORD   | The SAP B1 user password for the connection.                                                                                  |
| DBUSERNAME   | The username for the company database.                                                                                        |
| DBPASSWORD   | The password for the company password.                                                                                        |
| PRICELIST    | The price list to use for copying items to Woocommerce                                                                        |
| WOOURL       | The url of the woocommerce server                                                                                             |
| WOOKEY       | The secret credential supplied by woocommerce                                                                                 |
| WOOSECRET    | The secret credential supplied by woocommerce                                                                                 |

### Available Sap Versions

Populate `DIAPI` with one of these values

- SAPbobsCOM90
- SAPbobsCOM89
- SAPbobsCOM88
- SAPbobsCOM67
- SAPbobsCOM2007
- SAPbobsCOM2005
