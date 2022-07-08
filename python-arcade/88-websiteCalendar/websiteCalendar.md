<p>You're creating your own website for Harry Potter fans. As you all believe in magic, you're waiting for your personal letter from Hogwarts, that will definitely arrive to you some day with a magnificent owl. To be prepared for this exciting moment you decided to embed a calendar to your website on which you will mark the days when Hogwarts owls can bring letters.</p>
<p>Given a <code>month</code> and a <code>year</code>, return an HTML table representing the desired calendar. Follow the same format as provided in the example but <strong>omit all whitespace characters</strong> (i.e. tabs, newlines and whitespaces) where it is possible, because you care about space efficiency.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>month = 11</code> and <code>year = 2016</code>, the output should be</p>
<pre><code>solution(month, year) =
"&lt;table border="0" cellpadding="0" cellspacing="0" class="month"&gt;
  &lt;tr&gt;
    &lt;th colspan="7" class="month"&gt;November 2016&lt;/th&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;th class="mon"&gt;Mon&lt;/th&gt;
    &lt;th class="tue"&gt;Tue&lt;/th&gt;
    &lt;th class="wed"&gt;Wed&lt;/th&gt;
    &lt;th class="thu"&gt;Thu&lt;/th&gt;
    &lt;th class="fri"&gt;Fri&lt;/th&gt;
    &lt;th class="sat"&gt;Sat&lt;/th&gt;
    &lt;th class="sun"&gt;Sun&lt;/th&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td class="noday"&gt;&amp;nbsp;&lt;/td&gt;
    &lt;td class="tue"&gt;1&lt;/td&gt;
    &lt;td class="wed"&gt;2&lt;/td&gt;
    &lt;td class="thu"&gt;3&lt;/td&gt;
    &lt;td class="fri"&gt;4&lt;/td&gt;
    &lt;td class="sat"&gt;5&lt;/td&gt;
    &lt;td class="sun"&gt;6&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td class="mon"&gt;7&lt;/td&gt;
    &lt;td class="tue"&gt;8&lt;/td&gt;
    &lt;td class="wed"&gt;9&lt;/td&gt;
    &lt;td class="thu"&gt;10&lt;/td&gt;
    &lt;td class="fri"&gt;11&lt;/td&gt;
    &lt;td class="sat"&gt;12&lt;/td&gt;
    &lt;td class="sun"&gt;13&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td class="mon"&gt;14&lt;/td&gt;
    &lt;td class="tue"&gt;15&lt;/td&gt;
    &lt;td class="wed"&gt;16&lt;/td&gt;
    &lt;td class="thu"&gt;17&lt;/td&gt;
    &lt;td class="fri"&gt;18&lt;/td&gt;
    &lt;td class="sat"&gt;19&lt;/td&gt;
    &lt;td class="sun"&gt;20&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td class="mon"&gt;21&lt;/td&gt;
    &lt;td class="tue"&gt;22&lt;/td&gt;
    &lt;td class="wed"&gt;23&lt;/td&gt;
    &lt;td class="thu"&gt;24&lt;/td&gt;
    &lt;td class="fri"&gt;25&lt;/td&gt;
    &lt;td class="sat"&gt;26&lt;/td&gt;
    &lt;td class="sun"&gt;27&lt;/td&gt;
  &lt;/tr&gt;
  &lt;tr&gt;
    &lt;td class="mon"&gt;28&lt;/td&gt;
    &lt;td class="tue"&gt;29&lt;/td&gt;
    &lt;td class="wed"&gt;30&lt;/td&gt;
    &lt;td class="noday"&gt;&amp;nbsp;&lt;/td&gt;
    &lt;td class="noday"&gt;&amp;nbsp;&lt;/td&gt;
    &lt;td class="noday"&gt;&amp;nbsp;&lt;/td&gt;
    &lt;td class="noday"&gt;&amp;nbsp;&lt;/td&gt;
  &lt;/tr&gt;
&lt;/table&gt;"
</code></pre>
<p>Here is how this calendar would look on your website:</p>
<table class="month">
<tr><th colspan="7" class="month">November 2016</th></tr>
<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
<tr><td class="noday"> </td><td class="tue">1</td><td class="wed">2</td><td class="thu">3</td><td class="fri">4</td><td class="sat">5</td><td class="sun">6</td></tr>
<tr><td class="mon">7</td><td class="tue">8</td><td class="wed">9</td><td class="thu">10</td><td class="fri">11</td><td class="sat">12</td><td class="sun">13</td></tr>
<tr><td class="mon">14</td><td class="tue">15</td><td class="wed">16</td><td class="thu">17</td><td class="fri">18</td><td class="sat">19</td><td class="sun">20</td></tr>
<tr><td class="mon">21</td><td class="tue">22</td><td class="wed">23</td><td class="thu">24</td><td class="fri">25</td><td class="sat">26</td><td class="sun">27</td></tr>
<tr><td class="mon">28</td><td class="tue">29</td><td class="wed">30</td><td class="noday"> </td><td class="noday"> </td><td class="noday"> </td><td class="noday"> </td></tr>
</table>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer month</strong></p>
<p>1-based number of a month (i.e. <code>1</code> stands for January, <code>2</code> stands for February, and so on).</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ month ≤ 12</code>.</p>
</li>
<li>
<p><strong>[input] integer year</strong></p>
<p>4-digit number of a year. Please don't forget that in <a href="keyword://leap" target="_blank">leap</a> years February has <code>29</code> days.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1900 ≤ year ≤ 2100</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>An HTML table corresponding to the given month and the given year.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
