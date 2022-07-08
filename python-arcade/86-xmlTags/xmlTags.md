<p>You want to create your local database containing information about the things you find the coolest. You used to store this information in <code>xml</code> documents, so now you need to come up with an algorithm that will convert the existing format into the new one. First you decided to choose a structure for your scheme, and to do it you want to represent <code>xml</code> document as a tree, i.e. gather all the tags and print them out as follows:</p>
<pre><code>tag1()
 --tag1.1(attribute1, attribute2, ...)
 ----tag1.1.1(attribute1, attribute2, ...)
 ----tag1.1.2(attribute1, attribute2, ...)
 --tag1.2(attribute1, attribute2, ...)
 ----tag1.2.1(attribute1, attribute2, ...)
...
</code></pre>
<p>where attributes of each tag are sorted <a href="keyword://lexicographical-order-for-strings" target="_blank">lexicographically</a>.</p>
<p>You are a careful person, so the structure of the <code>xml</code> is neatly organized is such a way that:</p>
<ul>
<li>there is a single tag at the root level;</li>
<li>each tag has a single parent tag (i.e. if there are several occurrences of tag <code>a</code>, and in one occurrence it's a child of tag <code>b</code> and in the other one it's a child of tag <code>c</code>, then <code>b = c</code>);</li>
<li>each appearance of the same tag belongs to the same level.</li>
</ul>
<p>Given an <code>xml</code> file, return its structure as shown above. The tags of the same level should be sorted in the order they appear in <code>xml</code>, and the attributes should be sorted <em>lexicographically</em>.</p>
<p>Note: you are given xml represantation in one line.</p>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Example</span></p>
<p>For</p>
<pre><code>xml =
"&lt;data&gt;
    &lt;animal name="cat"&gt;
    	&lt;genus&gt;Felis&lt;/genus&gt;
        &lt;family name="Felidae" subfamily="Felinae"/&gt;
        &lt;similar name="tiger" size="bigger"/&gt;
    &lt;/animal&gt;
    &lt;animal name="dog"&gt;
        &lt;family name="Canidae" member="canid"/&gt;
        &lt;order&gt;Carnivora&lt;/order&gt;
        &lt;similar name="fox" size="similar"/&gt;
    &lt;/animal&gt;
&lt;/data&gt;"
</code></pre>
<p>the output should be</p>
<pre><code>solution(xml) =
["data()",
 "--animal(name)",
 "----genus()",
 "----family(member, name, subfamily)",
 "----similar(name, size)",
 "----order()"]
</code></pre>
<p><span class="markdown--header" style="color:#2b3b52;font-size:1.4em">Input/Output</span></p>
<ul>
<li>
<p><strong>[execution time limit] 4 seconds (py3)</strong></p>
</li>
<li>
<p><strong>[input] string xml</strong></p>
<p><code>xml</code> file as a string.</p>
<p><em>Guaranteed constraints:</em><br />
<code>7 ≤ xml.length ≤ 1000</code>.</p>
</li>
<li>
<p><strong>[output] array.string</strong></p>
<p>A list representing the structure of the <code>xml</code> file as described above.</p>
</li>
</ul>
<p><strong>[Python 3] Syntax Tips</strong></p>
<pre><code class="language-python"><span class="hljs-comment"># Prints help message to the console</span>
<span class="hljs-comment"># Returns a string</span>
<span class="hljs-keyword">def</span> <span class="hljs-title function_">helloWorld</span>(<span class="hljs-params">name</span>):
    <span class="hljs-built_in">print</span>(<span class="hljs-string">"This prints to the console when you Run Tests"</span>)
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + name

</code></pre>
