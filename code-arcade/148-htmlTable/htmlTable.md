<p>HTML tables allow web developers to arrange data into rows and columns of cells. They are created using the <code>&lt;table&gt;</code> tag. Its content consists of one or more rows denoted by the <code>&lt;tr&gt;</code> tag. Further, the content of each row comprises one or more cells denoted by the <code>&lt;td&gt;</code> tag, and content within the <code>&lt;td&gt;</code> tags is what site visitors see in the table. <em>For this task assume that tags have no attributes in contrast to real world HTML.</em></p>
<p>Some tables contain the <code>&lt;th&gt;</code> tag. This tag defines header cells, which shouldn't be counted as regular cells.</p>
<p>You are given a <strong>rectangular</strong> HTML table. Extract the content of the cell with coordinates <code>(row, column)</code>.</p>
<p>If you are not familiar with HTML, check out <a href="keyword://html-rules-for-tags" target="_blank">this note</a>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>table = "&lt;table&gt;&lt;tr&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;TWO&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;three&lt;/td&gt;&lt;td&gt;FoUr4&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;"</code>, <code>row = 0</code>, and <code>column = 1</code>, the output should be<br />
<code>solution(table, row, column) = "TWO"</code>.</p>
<pre><code>&lt;table&gt;
 &lt;tr&gt;
  &lt;td&gt;1&lt;/td&gt;
  &lt;td&gt;TWO&lt;/td&gt;
 &lt;/tr&gt;
 &lt;tr&gt;
  &lt;td&gt;three&lt;/td&gt;
  &lt;td&gt;FoUr4&lt;/td&gt;
 &lt;/tr&gt;
&lt;/table&gt;
</code></pre>
<p>corresponds to:</p><table><tr><td>1</td><td>TWO</td></tr><tr><td>three</td><td>FoUr4</td></tr></table><p></p>
</li>
<li>
<p>For <code>table = "&lt;table&gt;&lt;tr&gt;&lt;td&gt;1&lt;/td&gt;&lt;td&gt;TWO&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;"</code>, <code>row = 1</code>, and <code>column = 0</code>, the output should be<br />
<code>solution(table, row, column) = "No such cell"</code>.</p>
<pre><code>&lt;table&gt;
 &lt;tr&gt;
  &lt;td&gt;1&lt;/td&gt;
  &lt;td&gt;TWO&lt;/td&gt;
 &lt;/tr&gt;
&lt;/table&gt;
</code></pre>
<p>corresponds to:</p><table><tr><td>1</td><td>TWO</td></tr></table><p></p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string table</strong></p>
<p>A syntactically correct representation of a rectangular HTML table with at least one cell. Each of its cells contains only letters and/or digits.</p>
<p><em>Guaranteed constraints:</em><br />
<code>35 ≤ table.length ≤ 1600</code>.</p>
</li>
<li>
<p><strong>[input] integer row</strong></p>
<p>A non-negative integer representing 0-based index of the desired row (rows are numbered from top to bottom).</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ row ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] integer column</strong></p>
<p>A non-negative integer representing 0-based index of the desired column (columns are numbered from left to right).</p>
<p><em>Guaranteed constraints:</em><br />
<code>0 ≤ column ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] string</strong></p>
<p>The content of the cell with coordinates <code>(row, column)</code> or the string <code>"No such cell"</code> if there is no cell with those coordinates in the <code>table</code>.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
