<p>You've got tired of fixing your relatives' PCs after they visited some phishing website so you decided to implement a special plug-in for their browsers which will check if the page they are trying to visit is similar to the one in the blacklist.</p>
<p>For that, you've thought of the special algorithm that for two URLs <code>url1</code> and <code>url2</code> computes their similarity as following:</p>
<ol>
<li>Initially their similarity is <code>0</code></li>
<li>Then, it is increased by the following rules:</li>
</ol>
<ul>
<li><code>+5</code>, if the same protocol is used in both URLs.</li>
<li><code>+10</code>, if <code>url1</code> and <code>url2</code> have the same address.</li>
<li><code>+k</code>, if the <em>first</em> <code>k</code> components of <code>path</code> (delimited by <code>/</code>) are exactly the same (and in the same order) between the two URLs.</li>
<li><code>+1</code> if for each <code>varNames</code> common between them. Additional <code>+1</code> if the respective values are equal too.</li>
</ul>
<p>URLs are given in the following format: <code>protocol://address[(/path)*][?query]</code> (where <code>query = varName=value(&amp;varName=value)*</code>, parts given in <code>[]</code> are optional, and parts in <code>()*</code> may be repeated several times). Each of the named elements (i.e. <code>protocol</code>, <code>address</code>, <code>path</code>, <code>varName</code> and <code>value</code>) are guaranteed to contain only alphanumeric characters and periods.</p>
<p>Given the two URLs <code>url1</code> and <code>url2</code>, compute their similarity using the algorithm described above.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>url1 = "https://codesignal.com/home/test?param1=42&amp;param3=testing&amp;login=admin"
</code></pre>
<p>and</p>
<pre><code>url2 = "https://codesignal.com/home/secret/test?param3=fish&amp;param1=42&amp;password=admin"
</code></pre>
<p>the output should be<br />
<code>solution(url1, url2) = 19</code>.</p>
<p>Because these URLs have the same protocols, addresses, first path component (<code>home</code>) and two <code>varNames</code>, with one also having the same value in both of them.<br />
So the resulting similarity is thus <code>5 + 10 + 1 + 1 + 1 + 1 = 19</code>.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string url1</strong></p>
<p>First URL. It can only contain lowercase English letters, digits and characters <code>'.'</code>, <code>'/'</code>, <code>':'</code>, <code>'?'</code>, <code>'&amp;'</code> and <code>'='</code>.<br />
It's guaranteed that each <code>varName</code> is unique.</p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ url1.length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[input] string url2</strong></p>
<p>Second URL with the same format as <code>url1</code>.</p>
<p><em>Guaranteed constraints:</em><br />
<code>5 ≤ url2.length ≤ 100</code>.</p>
</li>
<li>
<p><strong>[output] integer</strong></p>
<p>The computed similarity.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
