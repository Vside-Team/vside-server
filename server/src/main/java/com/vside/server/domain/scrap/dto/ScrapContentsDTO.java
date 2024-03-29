package com.vside.server.domain.scrap.dto;

import lombok.*;

import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class ScrapContentsDTO {

    private Long contentId;
    private String title;
    private String contentLink;
    private String coverImgUrl;
    private String contentImgUrl;
    private List<String> keywords;
    private String dateTime;
    private boolean isScrap;

}
