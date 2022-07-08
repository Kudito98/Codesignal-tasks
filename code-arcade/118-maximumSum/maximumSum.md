<p>You are given an array of integers <code>a</code>. A <em>range sum query</em> is defined by a pair of non-negative integers <code>l</code> and <code>r</code> (<code>l &lt;= r</code>). The output to a <em>range sum query</em> on the given array <code>a</code> is the sum of all the elements of <code>a</code> that have indices from <code>l</code> to <code>r</code>, inclusive.</p>
<p>You have the array <code>a</code> and a list of <em>range sum queries</em> <code>q</code>. Find an algorithm that can rearrange the array <code>a</code> in such a way that the total sum of all of the query outputs is maximized, and return this total sum.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>a = [9, 7, 2, 4, 4]</code> and <code>q = [[1, 3], [1, 4], [0, 2]]</code>, the output should be<br />
<code>solution(a, q) = 62</code>.</p>
<p>You can get this sum if the array <code>a</code> is rearranged to be <code>[2, 9, 7, 4, 4]</code>. In that case, the first <em>range sum query</em> <code>[1, 3]</code> returns the sum <code>9 + 7 + 4 = 20</code>, the second query <code>[1, 4]</code> returns the sum <code>9 + 7 + 4 + 4 = 24</code>, and the third query <code>[0, 2]</code> returns the sum <code>2 + 9 + 7 = 18</code>. The total sum will be <code>20 + 24 + 18 = 62</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer a</strong></p>
<p>An initial array.</p>
<p><em>Guaranteed constraints:</em><br />
<code>2 ≤ a.length ≤ 10</code>,<br />
<code>1 ≤ a[i] ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] array.array.integer q</strong></p>
<p>An array of <em>range sum queries</em>, where each query is an array of two non-negative integers.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ q.length ≤ 10</code>,<br />
<code>0 ≤ q[i][0] ≤ q[i][1] &lt; a.length</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>Return the maximum possible total sum of the given <em>range sum query</em> outputs.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
