<p>You are given an array of integers that you want distribute between several groups. The first group should contain numbers from <code>1</code> to <code>10<sup>4</sup></code>, the second should contain those from <code>10<sup>4</sup> + 1</code> to <code>2 * 10<sup>4</sup></code>, ..., the <code>100<sup>th</sup></code> one should contain numbers from <code>99 * 10<sup>4</sup> + 1</code> to <code>10<sup>6</sup></code> and so on.</p>
<p>All the numbers will then be written down in groups to the text file in such a way that:</p>
<ul>
<li>the groups go one after another;</li>
<li>each non-empty group has a header which occupies one line;</li>
<li>each number in a group occupies one line.</li>
</ul>
<p>Calculate how many lines the resulting text file will have.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For <code>a = [20000, 239, 10001, 999999, 10000, 20566, 29999]</code>, the output should be<br />
<code>solution(a) = 11</code>.</p>
<p>The numbers can be divided into <code>4</code> groups:</p>
<ul>
<li><code>239</code> and <code>10000</code> go to the <code>1<sup>st</sup></code> group (<code>1 ... 10<sup>4</sup></code>);</li>
<li><code>10001</code> and <code>20000</code> go to the second <code>2<sup>nd</sup></code> (<code>10<sup>4</sup> + 1 ... 2 * 10<sup>4</sup></code>);</li>
<li><code>20566</code> and <code>29999</code> go to the <code>3<sup>rd</sup></code> group (<code>2 * 10<sup>4</sup> + 1 ... 3 * 10<sup>4</sup></code>);</li>
<li>groups from <code>4</code> to <code>99</code> are empty;</li>
<li><code>999999</code> goes to the <code>100<sup>th</sup></code> group (<code>99 * 10<sup>4</sup> + 1 ... 10<sup>6</sup></code>).</li>
</ul>
<p>Thus, there will be <code>4</code> groups (i.e. four headers) and <code>7</code> numbers, so the file will occupy <code>4 + 7 = 11</code> lines.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] array.integer a</strong></p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ a.length ≤ 10<sup>5</sup></code>,<br />
<code>1 ≤ a[i] ≤ 10<sup>9</sup></code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The number of lines needed to store the grouped numbers.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
