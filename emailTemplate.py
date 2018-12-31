html = """<head>
    <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
    <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
    <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
</head>

<body>
    <div id="mailsub" class="notification" align="center">

        <table width="100%" border="0" cellspacing="0" cellpadding="0" style="min-width: 320px;">
            <tr>
                <td align="center" bgcolor="#eff3f8">
            <tr>
                <td align="center" bgcolor="#fbfcfd">
                    <table width="90%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                            <td align="center">
                                <!-- padding -->
                                    <img src="cid:image1" alt="weather-icon" border="0" style="width:120px;height:120px;" />
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                        <tr>
                            <td align="center">
                                <div style="line-height: 12px;">
                                    <font face="Arial, Helvetica, sans-serif" size="5" color="#57697e" style="font-size: 16px;">
                                        <span style="font-family: Arial, Helvetica, sans-serif; font-size: 16px; color: #57697e;">
                                            <p>Daily Summary: {3}</p>
                                            <p>Current Temperature: {0} degrees</p>
                                            <p>Feels like: {1} degrees</p>
                                            <p>Wind Speed: {2}mph</p>
                                        </span></font>
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <!--content 1 END-->
            <tr>
                <td align="center" bgcolor="#fbfcfd">
                    <table width="90%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                            <td align="center">
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                                <div style="line-height: 22px;">
                                    <img src="cid:image2" alt="quote-icon" border="0" style="width:120px;height:120px;" />
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                        <tr>
                            <td align="center">
                                <div style="line-height: 12px;">
                                    <font face="Arial, Helvetica, sans-serif" size="5" color="#57697e" style="font-size: 22px;">
                                        <span style="font-family: Arial, Helvetica, sans-serif; font-size: 16px; color: #57697e;">
                                            {6}
                                        </span></font>
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                        <tr>
                            <td align="center">
                                <div style="line-height: 24px;">
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <!--content 1a END-->
            <tr>
                <td align="center" bgcolor="#fbfcfd">
                    <table width="90%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                            <td align="center">
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                                <div style="line-height: 22px;">
                                    <img src="cid:image3" alt="til-icon" border="0" style="width:120px;height:120px;" />
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                        <tr>
                            <td align="center">
                                <div style="line-height: 12px;">
                                    <font face="Arial, Helvetica, sans-serif" size="5" color="#57697e" style="font-size: 22px;">
                                        <span style="font-family: Arial, Helvetica, sans-serif; font-size: 16px; color: #57697e;">
                                            {4}
                                            <p>-{5}</p>
                                        </span></font>
                                </div>
                                <!-- padding -->
                                <div style="height: 40px; line-height: 40px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                        <tr>
                            <td align="center">
                                <div style="line-height: 24px;">
                                </div>
                                <!-- padding -->
                                <div style="height: 10px; line-height: 10px; font-size: 10px;"> </div>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <!--content 1b END-->
        </td>
        </tr>
        </table>
</body>

</html>"""