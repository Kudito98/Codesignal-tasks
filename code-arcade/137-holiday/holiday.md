<p>John Doe likes solutions very much, and he was very happy to hear that his country's government decided to introduce yet another one. He heard that the new solution will be celebrated each year on the <code>x<sup>th</sup></code> week of <code>month</code>, on <code>weekDay</code>.</p>
<p>Your task is to return the day of <code>month</code> on which the solution will be celebrated in the year <code>yearNumber</code>.</p>
<p>For your convenience, here are the lists of months names and lengths and the list of days of the week names.</p>
<ul>
<li>Months: <code>"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"</code>.</li>
<li>Months lengths: <code>31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31</code>.</li>
<li>Days of the week: <code>"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"</code>.</li>
</ul>
<p>Please, note that in <a href="keyword://leap" target="_blank">leap years</a> February has <code>29</code> days.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>x = 3</code>, <code>weekDay = "Wednesday"</code>, <code>month = "November"</code>, and <code>yearNumber = 2016</code>, the output should be<br />
<code>solution(x, weekDay, month, yearNumber) = 16</code>.</p>
<p>The new solution will be celebrated every November on the <code>3<sup>rd</sup></code> Wednesday of the month. In 2016 the <code>3<sup>rd</sup></code> Wednesday falls on the <code>16<sup>th</sup></code> of November.</p>
</li>
<li>
<p>For <code>x = 5</code>, <code>weekDay = "Thursday"</code>, <code>month = "November"</code>, and <code>yearNumber = 2016</code>, the output should be<br />
<code>solution(x, weekDay, month, yearNumber) = -1</code>.</p>
<p>There are only 4 Thursdays in November 2016.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] integer x</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ x ≤ 5</code>.</p>
</li>
<li>
<p><strong>[input] string weekDay</strong></p>
<p>A string representing a correct name of some day of the week.</p>
<p><em>Guaranteed constraints:</em><br />
<code>weekDay ∈ {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}</code>.</p>
</li>
<li>
<p><strong>[input] string month</strong></p>
<p>A string representing a correct name of some month.</p>
<p><em>Guaranteed constraints:</em><br />
<code>month ∈ {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"}</code>.</p>
</li>
<li>
<p><strong>[input] integer yearNumber</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>2015 ≤ yearNumber ≤ 2500</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The day of <code>month</code> on which the holiday will be celebrated in the year <code>yearNumber</code>. If there is no answer, return <code>-1</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
