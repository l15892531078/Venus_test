# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from Venus.tools.other_library.selenium.webdriver.firefox.webdriver import WebDriver as Firefox  # noqa
from Venus.tools.other_library.selenium.webdriver.firefox.firefox_profile import FirefoxProfile  # noqa
from Venus.tools.other_library.selenium.webdriver.firefox.options import Options as FirefoxOptions  # noqa
from Venus.tools.other_library.selenium.webdriver.chrome.webdriver import WebDriver as Chrome  # noqa
from Venus.tools.other_library.selenium.webdriver.chrome.options import Options as ChromeOptions  # noqa
from Venus.tools.other_library.selenium.webdriver.ie.webdriver import WebDriver as Ie  # noqa
from Venus.tools.other_library.selenium.webdriver.ie.options import Options as IeOptions  # noqa
from Venus.tools.other_library.selenium.webdriver.edge.webdriver import WebDriver as Edge  # noqa
from Venus.tools.other_library.selenium.webdriver.opera.webdriver import WebDriver as Opera  # noqa
from Venus.tools.other_library.selenium.webdriver.safari.webdriver import WebDriver as Safari  # noqa
from Venus.tools.other_library.selenium.webdriver.blackberry.webdriver import WebDriver as BlackBerry  # noqa
from Venus.tools.other_library.selenium.webdriver.phantomjs.webdriver import WebDriver as PhantomJS  # noqa
from Venus.tools.other_library.selenium.webdriver.android.webdriver import WebDriver as Android  # noqa
from Venus.tools.other_library.selenium.webdriver.webkitgtk.webdriver import WebDriver as WebKitGTK # noqa
from Venus.tools.other_library.selenium.webdriver.webkitgtk.options import Options as WebKitGTKOptions # noqa
from Venus.tools.other_library.selenium.webdriver.remote.webdriver import WebDriver as Remote  # noqa
from Venus.tools.other_library.selenium.webdriver.common.desired_capabilities import DesiredCapabilities  # noqa
from Venus.tools.other_library.selenium.webdriver.common.action_chains import ActionChains  # noqa
from Venus.tools.other_library.selenium.webdriver.common.touch_actions import TouchActions  # noqa
from Venus.tools.other_library.selenium.webdriver.common.proxy import Proxy  # noqa

__version__ = '3.14.1'
