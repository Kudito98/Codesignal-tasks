<p>Consider a string containing only letters and whitespaces. It is allowed to replace some (possibly, none) whitespaces with newline symbols to obtain a multiline text. Call a multiline text <em>beautiful</em> if and only if each of its lines (i.e. <a href="keyword://substring" target="_blank">substrings</a> delimited by a newline character) contains an equal number of characters (only letters and whitespaces should be taken into account when counting the total while newline characters shouldn't). Call the length of the line the <em>text width</em>.</p>
<p>Given a string and some integers <code>l</code> and <code>r</code> (<code>l ≤ r</code>), check if it's possible to obtain a beautiful text from the string with a text width that's within the range <code>[l, r]</code>.</p>
<p><strong>Example</strong></p>
<ul>
<li>
<p>For <code>inputString = "Look at this example of a correct text"</code>, <code>l = 5</code>, and <code>r = 15</code>, the output should be<br />
<code>solution(inputString, l, r) = true</code>.</p>
<p>We can replace <code>13<sup>th</sup></code> and <code>26<sup>th</sup></code> characters with <code>'\n'</code>, and obtain the following multiline text of width <code>12</code>:</p>
<pre><code>Look at this
example of a
correct text
</code></pre>
</li>
<li>
<p>For <code>inputString = "abc def ghi"</code>, <code>l = 4</code>, and <code>r = 10</code>, the output should be<br />
<code>solution(inputString, l, r) = false</code>.</p>
<p>There are two ways to obtain a text with lines of equal length from this input, one has <code>width = 3</code> and another has <code>width = 11</code> (this is a one-liner). Both of these values are not within our bounds.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string inputString</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>10 ≤ inputString.length ≤ 40</code>.</p>
</li>
<li>
<p><strong>[input] integer l</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ l ≤ r</code>.</p>
</li>
<li>
<p><strong>[input] integer r</strong></p>
<p>A positive integer.</p>
<p><em>Guaranteed constraints:</em><br />
<code>l ≤ r ≤ 15</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
