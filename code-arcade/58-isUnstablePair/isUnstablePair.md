<p>Some file managers sort filenames taking into account case of the letters, others compare strings as if all of the letters are of the same case. That may lead to different ways of filename ordering.</p>
<p>Call two filenames <em>an unstable pair</em> if their ordering depends on the case.</p>
<p>To compare two filenames <code>a</code> and <code>b</code>, find the first position <code>i</code> at which <code>a[i] ≠ b[i]</code>. If <code>a[i] &lt; b[i]</code>, then <code>a &lt; b</code>. Otherwise <code>a &gt; b</code>. If such position doesn't exist, the shorter string goes first.</p>
<p>Given two filenames, check whether they form an unstable pair.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<ul>
<li>
<p>For <code>filename1 = "aa"</code> and <code>filename2 = "AAB"</code>, the output should be<br />
<code>solution(filename1, filename2) = true</code>.</p>
<p>Because <code>"AAB" &lt; "aa"</code>, but <code>"AAB" &gt; "AA"</code>.</p>
</li>
<li>
<p>For <code>filename1 = "A"</code> and <code>filename2 = "z"</code>, the output should be<br />
<code>solution(filename1, filename2) = false</code>.</p>
<p>Both <code>"A" &lt; "z"</code> and <code>"a" &lt; "z"</code>.</p>
</li>
</ul>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string filename1</strong></p>
<p>A non-empty string of English letters and digits.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ filename1.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[input] string filename2</strong></p>
<p>A non-empty string of English letters and digits. It's guaranteed that there is no ambiguity, i.e. even being considered in the same case strings are never equal.</p>
<p><em>Guaranteed constraints:</em><br />
<code>1 ≤ filename2.length ≤ 10</code>.</p>
</li>
<li>
<p><strong>[output] boolean</strong></p>
<p><code>true</code> if <code>filename1</code> and <code>filename2</code> form an unstable pair, <code>false</code> otherwise.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
