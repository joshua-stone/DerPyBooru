#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

class Search(object):
  def __init__(self, q=[], page=1, perpage=15, comments=False, fav=False, key=""):
    self.__parameters = {}
    self.q = q
    self.page = page
    self.perpage = perpage
    self.comments = comments
    self.fav = fav
    self.key = key

  @property
  def hostname(self):
    return("https://derpiboo.ru")

  @property
  def q(self):
    return(self.parameters["q"])

  @q.setter
  def q(self, q=[]):
    if not isinstance(q, list):
      raise TypeError("tags must be a list of strings")

    for tag in q:
      if not isinstance(tag, str):
        raise TypeError("{0} is not a string".format(tag))

      if "," in tag or tag == "":
        raise ValueError("tags can't contain commas or be empty strings")

    self.__parameters["q"] = [tag.strip() for tag in q]

  @property
  def page(self):
    return(self.parameters["page"])

  @page.setter
  def page(self, page=1):
    if not isinstance(page, int):
      raise TypeError("page number must be an int")

    if page < 1:
      raise ValueError("page number must be greater than 0")

    self.__parameters["page"] = page

  def next_page(self, number=1):
    if not isinstance(number, int):
      raise TypeError("page number must be an int")

    if number < 1:
      raise ValueError("page number must be greater than 0")

    self.__parameters["page"] += number

  def previous_page(self, number=1):
    if not isinstance(number, int):
      raise TypeError("page number must be an int")

    if number < 1:
      raise ValueError("page number must be greater than 0")

    if self.parameters["page"] - number <= 1:
      self.__parameters["page"] = 1
    else:
      self.__parameters["page"] -= number

  @property
  def perpage(self):
    return(self.parameters["perpage"])

  @perpage.setter
  def perpage(self, page_size):
    if not isinstance(page_size, int):
      raise TypeError("perpage must be an int")
    if page_size < 1 or page_size > 50:
      raise ValueError("perpage must be within range of 1-50")

    self.__parameters["perpage"] = page_size

  @property
  def comments(self):
    return(self.parameters["comments"])

  @comments.setter
  def comments(self, comments=True):
    if not isinstance(comments, bool):
      raise TypeError("comments must be either True or False")

    self.__parameters["comments"] = comments

  @property
  def key(self):
    return(self.parameters["key"])

  @key.setter
  def key(self, key=""):
    if not isinstance(key, str):
      raise TypeError("key must be a string") 

    self.__parameters["key"] = key

  @property
  def fav(self):
    return(self.parameters["fav"])

  @fav.setter
  def fav(self, fav=True):
    if not isinstance(fav, bool):
      raise TypeError("favorites must be either True or False")

    self.__parameters["fav"] = fav

  @property
  def parameters(self):
    return(self.__parameters)

  @property
  def url(self):
    parameters = []

    if self.q == []:
      search = "/images/page/{0}.json".format(self.page)
    else:
      search, tags = "/search.json", ",".join(self.q)
      parameters.append("q={0}".format(tags.replace(" ", "+")))
      parameters.append("page={0}".format(self.page))

    if self.comments == True:
      parameters.append("comments=")

    if self.fav == True:
      parameters.append("fav=")

    parameters.append("perpage={0}".format(self.parameters["perpage"]))

    url = (self.hostname + search)

    if parameters != []:
      url += "?{0}".format("&".join(parameters))

    return(url)

