package com.vside.server.domain.auth.dto;

import com.vside.server.domain.common.LoginType;
import io.swagger.annotations.ApiModelProperty;
import lombok.*;

import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class LoginRequest {
    @NotNull @ApiModelProperty(required = true, example = "KAKAO")
    private LoginType provider;

    @NotBlank @ApiModelProperty(required = true)
    private String snsId;
}
