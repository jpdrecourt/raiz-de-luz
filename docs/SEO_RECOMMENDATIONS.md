# Raiz de Luz Website - SEO Recommendations & Action Plan

**Date:** November 24, 2025
**Site:** https://raizdeluz.eu
**Status:** Solid foundation with critical infrastructure gaps now resolved

---

## Overview

The Raiz de Luz website has successfully completed its critical SEO infrastructure setup:
- ✅ `sitemap.xml` - Created and deployed
- ✅ `robots.txt` - Created and deployed

This document outlines the remaining high-impact recommendations to maximize search visibility and organic traffic potential.

---

## Recommendations by Priority

### 🟠 High Impact (Implement Next)

#### 1. Add JSON-LD Structured Data
**Why:** Search engines use structured data to understand your business better. This enables rich snippets in search results (ratings, hours, phone numbers).

**Implementation:**
- Add LocalBusiness schema to `contacto.html` with business hours, phone, address, and location
- Add Organization schema to `index.html` with company name, logo, and social profiles
- Add Service schema to each service detail section

**Example for LocalBusiness schema (add to contacto.html `<head>`):**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "LocalBusiness",
  "name": "Raiz de Luz",
  "image": "https://raizdeluz.eu/media/raiz-de-luz-logo.png",
  "description": "Massagem Xamânica e Bem-Estar",
  "telephone": "+351912615772",
  "email": "info@raizdeluz.eu",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "[Rua/Avenida e Número]",
    "postalCode": "[Código Postal]",
    "addressLocality": "[Cidade]",
    "addressCountry": "PT"
  },
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "opens": "10:00",
      "closes": "19:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": "Saturday",
      "opens": "10:00",
      "closes": "14:00"
    }
  ],
  "url": "https://raizdeluz.eu"
}
</script>
```

**Effort:** 2-3 hours | **Expected Impact:** Medium-High

---

#### 2. Complete All Placeholder Content
**Why:** Incomplete content signals low quality to search engines and confuses visitors. Current placeholders:
- Service prices showing "€XX"
- Therapist bios with "[Breve biografia...]"
- Address incomplete with "[Rua/Avenida]"
- Map placeholder not replaced with actual Google Map

**Action Items:**
- [ ] Update all service prices in `servicos.html`
- [ ] Write complete therapist biographies in `sobre.html`
- [ ] Fill in complete address in `contacto.html`
- [ ] Embed actual Google Map (replace placeholder with iframe)

**Effort:** 2-4 hours | **Expected Impact:** High (content quality)

---

#### 3. Implement Breadcrumb Navigation
**Why:** Improves user experience and provides additional internal linking signals. Helps users understand site structure.

**Implementation:**
- Add breadcrumb schema markup using JSON-LD
- Display breadcrumbs above main content on subpages
- Example structure: Home > Serviços > Massagem Xamânica

**Location:** Add to top of `<main>` on servicos.html, sobre.html, contacto.html

**Effort:** 1-2 hours | **Expected Impact:** Low-Medium (UX improvement)

---

#### 4. Add Service Schema Markup
**Why:** Enables rich snippets for each service. Search engines can display detailed service information in results.

**Implementation:**
Add to each service detail section in `servicos.html`:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "Service",
  "name": "Massagem Xamânica",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Raiz de Luz"
  },
  "description": "Massagem de cura profunda que combina técnicas tradicionais com trabalho energético",
  "areaServed": "PT",
  "availableChannel": {
    "@type": "ServiceChannel",
    "serviceUrl": "https://raizdeluz.eu/contacto.html"
  }
}
</script>
```

**Effort:** 1-2 hours (per service) | **Expected Impact:** Medium

---

### 🟡 Medium Impact (Plan for Next Month)

#### 5. Create Legal Pages
**Why:** Trust signals for search engines and visitors. Legally required for data collection (contact form).

**Pages to create:**
- `privacidade.html` - Privacy Policy (required for GDPR compliance - you collect form data)
- `termos.html` - Terms of Service
- `politica-cookies.html` - Cookie Policy (especially with GoatCounter analytics)

**Content to include:**
- Clear data handling practices
- How you use contact form submissions
- Google Analytics/GoatCounter data usage
- GDPR compliance statements
- Contact information for data requests

**Effort:** 3-4 hours | **Expected Impact:** High (legal + trust)

---

#### 6. Create FAQ Schema
**Why:** Your contacto.html already has FAQ content. Structured data markup enables special search result formatting.

**Current FAQs on contacto.html:**
- Como posso marcar uma sessão?
- Qual é a política de cancelamento?
- Preciso de trazer alguma coisa?
- Aceitam pagamento por Multibanco/MB Way?
- As sessões são adequadas para todos?

**Action:** Wrap existing FAQ section with JSON-LD FAQ schema markup

**Effort:** 1 hour | **Expected Impact:** Low-Medium (featured snippets)

---

#### 7. Implement Telephone & Email Schema
**Why:** Makes contact information clickable and recognized by search engines.

**Locations:**
- All pages have phone/email in footer
- contacto.html has dedicated contact section

**Action:** Add microdata markup to contact information:
```html
<a href="tel:+351912615772">
  <span itemscope itemtype="https://schema.org/Thing">
    <span itemprop="telephone">+351 912 615 772</span>
  </span>
</a>
```

**Effort:** 30 minutes | **Expected Impact:** Low (UX + accessibility)

---

### 🟢 Lower Priority (Quarterly Reviews)

#### 8. Start a Blog/Resources Section
**Why:** Opportunity to target long-tail keywords and provide value to visitors.

**Content Ideas:**
- "Benefícios da Massagem Xamânica" (benefits + tips)
- "Como Preparar-se para uma Sessão de Cura Energética"
- "Entender os Chakras: Guia Completo"
- "Bem-estar no Trabalho: Técnicas Rápidas"
- "Sustentabilidade e Práticas Holísticas"

**Implementation:** Would require adding a `/blog/` directory with blog post pages and listing page

**Effort:** 4-8 hours per post + 2-3 hours for blog structure | **Expected Impact:** Medium-High (long-term traffic)

---

#### 9. Add Testimonials with Schema
**Why:** Social proof improves conversion and can be displayed in rich snippets.

**Current Status:** Testimonials section exists (rdl-testimonials-section snippet)

**Action:** Add AggregateRating or Review schema markup to testimonial section

**Effort:** 1-2 hours | **Expected Impact:** Medium (conversion + trust)

---

#### 10. Optimize Images for Web
**Why:** Images are often not optimized, slowing down page load times.

**Actions:**
- Compress existing images (JPEG/PNG optimization)
- Consider WebP format for modern browsers
- Verify all images have descriptive alt text and filenames
- Use descriptive filenames: `massagem-xamanica.jpg` instead of `image1.jpg`

**Tools to use:**
- TinyPNG/Compressor for compression
- ImageMagick or Squoosh for WebP conversion

**Effort:** 2-3 hours | **Expected Impact:** Medium (Core Web Vitals)

---

#### 11. Create Hreflang Tags (If Applicable)
**Why:** If you plan to target both pt-PT and pt-BR markets.

**Implementation:** Add to `<head>` of all pages:
```html
<link rel="alternate" hreflang="pt-PT" href="https://raizdeluz.eu/index.html" />
<link rel="alternate" hreflang="pt-BR" href="https://raizdeluz.br/index.html" /> <!-- if applicable -->
<link rel="alternate" hreflang="x-default" href="https://raizdeluz.eu/index.html" />
```

**Effort:** 1 hour (if applicable) | **Expected Impact:** Low (unless multi-regional)

---

#### 12. Implement Twitter Card Metadata
**Why:** Better social media sharing experience and brand visibility.

**Add to `<head>` of pages:**
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@raizdeluz">
<meta name="twitter:title" content="Page Title">
<meta name="twitter:description" content="Page description">
<meta name="twitter:image" content="https://raizdeluz.eu/media/image.jpg">
```

**Effort:** 1 hour | **Expected Impact:** Low (social sharing)

---

---

## Technical SEO Checklist

| Item | Current Status | Next Steps |
|------|---|---|
| Mobile responsive | ✅ Complete | Monitor Core Web Vitals |
| HTTPS/SSL | ⚠️ Verify | Ensure domain has SSL certificate |
| Page load speed | ⚠️ Optimize | Implement image optimization |
| Crawlable structure | ✅ Complete | Monitor robots.txt effectiveness |
| Indexable content | ✅ Complete | Sitemap & robots.txt deployed |
| Meta descriptions | ✅ Complete | Review length (155-160 chars) |
| Unique titles | ✅ Complete | Ensure all are unique and compelling |
| Heading hierarchy | ✅ Complete | Maintain H1-H4 structure |
| Internal linking | ✅ Complete | Add breadcrumbs for deeper structure |
| Image optimization | ⚠️ Pending | Compress and use descriptive alt text |
| Analytics | ✅ Complete | GoatCounter tracking active |
| Sitemaps | ✅ Complete | sitemap.xml deployed |
| Robots.txt | ✅ Complete | robots.txt deployed |
| Schema markup | ⚠️ In progress | Add LocalBusiness, Organization, Service schemas |
| Structured data | ⚠️ Pending | Implement FAQ, Breadcrumb, Service schemas |
| Legal pages | ❌ Missing | Create Privacy, Terms, Cookie policies |

---

## Keyword Optimization Strategy

### Target Keywords by Category

#### Primary Service Keywords
- "Massagem xamânica Portugal"
- "Cura energética"
- "Bem-estar holístico"
- "Terapia sacro craniana"
- "Drenagem linfática"
- "Massagem desportiva"

#### Local Keywords (Recommended)
- "Massagem [sua cidade]"
- "Terapias [sua cidade]"
- "Cura energética [região]"
- "Bem-estar [sua cidade]"

#### Long-Tail Keywords (Lower competition)
- "Massagem para grávidas [cidade]"
- "Massagem xamânica benefícios"
- "Como encontrar bom terapeuta"
- "Terapias complementares Portugal"
- "Relaxamento e bem-estar [cidade]"

### Implementation Strategy
1. **Homepage:** Focus on primary keywords (massagem xamânica, bem-estar holístico)
2. **Servicos.html:** Each service section targets its specific service keyword
3. **Sobre.html:** Target trust-building keywords (experiência, qualificações, filosofia)
4. **Contacto.html:** Target local keywords (localização, agendamento, contacto)
5. **Future blog:** Target long-tail and educational keywords

---

## Action Plan Timeline

### Week 1 (Immediate)
- [x] Create sitemap.xml
- [x] Create robots.txt
- [ ] Complete all placeholder content
- [ ] Submit sitemap to Google Search Console

### Week 2-3 (This Month)
- [ ] Add JSON-LD schemas (LocalBusiness, Organization, Service)
- [ ] Implement breadcrumb navigation
- [ ] Add FAQ schema markup
- [ ] Optimize and compress images

### Week 4 (End of Month)
- [ ] Create legal pages (Privacy, Terms, Cookies)
- [ ] Set up Google Search Console if not done
- [ ] Implement Twitter Card metadata
- [ ] Review all changes and test

### Month 2 (December)
- [ ] Monitor search console for indexing
- [ ] Create first blog posts (2-3)
- [ ] Add testimonial schema
- [ ] Implement hreflang if multi-regional

### Ongoing (Quarterly)
- [ ] Monitor keyword rankings
- [ ] Analyze traffic patterns
- [ ] Update blog with new content (1-2 posts/month)
- [ ] Review and update old content
- [ ] Check Core Web Vitals performance

---

## Search Engine Submission Checklist

### Required Actions
1. **Google Search Console**
   - [ ] Verify domain ownership
   - [ ] Submit sitemap
   - [ ] Monitor indexing status
   - [ ] Check for crawl errors
   - [ ] View search performance data

2. **Bing Webmaster Tools**
   - [ ] Verify domain ownership
   - [ ] Submit sitemap
   - [ ] Monitor crawling

3. **Other Search Engines** (Optional)
   - [ ] Yandex (if targeting Russian speakers)
   - [ ] Baidu (if targeting Chinese speakers)

---

## Tools for SEO Monitoring

### Free Tools
- **Google Search Console** - Indexing, keywords, errors
- **Google Analytics** - Traffic, user behavior (complementary to GoatCounter)
- **Google PageSpeed Insights** - Performance metrics
- **Screaming Frog SEO Spider** - Technical SEO audit
- **Ubersuggest** - Keyword research (free tier)
- **Moz Local** - Local SEO verification

### Recommended Tools (Paid)
- **Ahrefs** - Comprehensive SEO analysis, backlinks
- **SEMrush** - Competitor analysis, keyword research
- **Moz Pro** - Rank tracking, site audit
- **Surfer SEO** - Content optimization guidance

---

## Common SEO Mistakes to Avoid

1. **Duplicate Content** - Ensure each page has unique content and title/meta
2. **Keyword Stuffing** - Write naturally; don't force keywords
3. **Thin Content** - Each page should provide real value (aim for 300+ words minimum)
4. **Poor Mobile Experience** - You're good here, but keep testing
5. **Broken Links** - Regularly check internal and external links
6. **Missing Alt Text** - Always describe images for accessibility + SEO
7. **Ignoring Search Console** - Check it weekly for errors/opportunities
8. **Not Tracking Results** - Monitor rankings and traffic changes

---

## Expected Results Timeline

### 1-3 Months
- Search engines fully crawl and index all pages
- Some keyword impressions in search results
- Initial traffic from branded searches

### 3-6 Months
- Ranking improvements for local keywords
- Increased organic traffic from service-specific searches
- Visibility in "near me" searches (with proper schema)

### 6-12 Months
- Established rankings for primary keywords
- Traffic growth from blog content (if implemented)
- Better conversion from optimized CTAs and trust signals

### 12+ Months
- Consistent organic traffic growth
- Authority building for competitive keywords
- Potential to rank for broader keywords

**Note:** Results depend on competition, execution quality, and content updates.

---

## Success Metrics to Track

### Essential Metrics
- **Organic traffic** (from Google Analytics or GoatCounter)
- **Keyword rankings** (Google Search Console)
- **Click-through rate (CTR)** from search results
- **Bounce rate** (quality of traffic)
- **Conversion rate** (form submissions, contact requests)

### Secondary Metrics
- **Pages per session** (engagement)
- **Average session duration** (content quality)
- **Backlinks** (domain authority)
- **Core Web Vitals** (page experience)

### Monthly Review
- Check Google Search Console impressions & clicks
- Review traffic trends
- Identify top-performing pages
- Note new keywords attracting traffic

---

## Conclusion

Your website has a solid SEO foundation with critical infrastructure now in place (sitemap.xml and robots.txt). By implementing the high-priority recommendations above, you can significantly improve:

- **Search visibility** - Better indexing and ranking
- **User experience** - Breadcrumbs, structured data, complete information
- **Trust signals** - Legal pages, testimonials, business information
- **Conversion rate** - Clear CTAs, complete information, social proof

**Recommended next step:** Complete placeholder content and implement JSON-LD schemas within the next 2 weeks. These will have the highest immediate impact on search visibility.

For questions about any recommendation, refer to the relevant section in this document or consult the linked schema.org documentation.

---

**Document Last Updated:** November 24, 2025
**Next Review Date:** December 24, 2025
